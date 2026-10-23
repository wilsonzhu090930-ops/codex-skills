#!/usr/bin/env python3
"""Inventory, apply and verify human/agent-authored Chinese UI summaries.

No network, model API, background process, application cache or credential access.
Requires PyYAML. Translation is performed by the agent using the SKILL.md workflow.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import yaml


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_skill(folder):
    path = folder / 'SKILL.md'
    if not path.is_file():
        raise ValueError(f'Missing SKILL.md: {folder}')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', path.read_text(), re.S)
    if not match:
        raise ValueError(f'Missing frontmatter: {path}')
    meta = yaml.safe_load(match[1])
    if not isinstance(meta, dict) or not meta.get('name') or not meta.get('description'):
        raise ValueError(f'Invalid skill metadata: {path}')
    return meta


def scan(roots):
    result, seen = [], set()
    for root in roots:
        root = Path(root).expanduser().resolve()
        folders = [root] if (root / 'SKILL.md').is_file() else sorted(p for p in root.iterdir() if p.is_dir()) if root.is_dir() else []
        for folder in folders:
            if not (folder / 'SKILL.md').is_file() or folder.resolve() in seen:
                continue
            # A root is an explicit trust boundary: do not follow links outside it.
            if not folder.resolve().is_relative_to(root):
                continue
            seen.add(folder.resolve())
            meta = read_skill(folder)
            ui_path = folder / 'agents/openai.yaml'
            ui = yaml.safe_load(ui_path.read_text()) if ui_path.is_file() else {}
            interface = (ui or {}).get('interface') or {}
            current = interface.get('short_description') or (meta.get('metadata') or {}).get('short-description') or meta['description']
            result.append({'path': str(folder.resolve()), 'name': meta['name'], 'description': meta['description'], 'current_summary': current, 'needs_chinese': not bool(re.search('[\u4e00-\u9fff]', str(current)))})
    return result


def prepare(plan):
    updates, seen = [], set()
    for entry in plan:
        folder = Path(entry['path']).expanduser().resolve()
        read_skill(folder)
        summary = entry['summary']
        if not isinstance(summary, str) or not 4 <= len(summary) <= 28 or '\n' in summary or '\r' in summary or not re.search('[\u4e00-\u9fff]', summary):
            raise ValueError('Summary must be one Chinese line of 4–28 characters')
        path = folder / 'agents/openai.yaml'
        if path.parent.is_symlink() or path.is_symlink():
            raise ValueError(f'Refusing linked UI metadata: {path}')
        if path in seen:
            raise ValueError(f'Duplicate plan target: {path}')
        seen.add(path)
        original = path.read_bytes() if path.exists() else None
        text = original.decode('utf-8') if original is not None else ''
        old = yaml.safe_load(text) or {}
        if not isinstance(old, dict) or not isinstance(old.get('interface', {}), dict):
            raise ValueError(f'Invalid interface: {path}')
        value = json.dumps(summary, ensure_ascii=False)
        if 'short_description' in old.get('interface', {}):
            # Refuse multiline summaries rather than rewriting other YAML fields.
            pattern = r'(?m)^(  short_description:) ([^\r\n]*)$'
            match = re.search(pattern, text)
            if not match or match[2].startswith(('|', '>')):
                raise ValueError(f'Unsupported summary formatting: {path}')
            new, count = re.subn(pattern, lambda m: m[1] + ' ' + value, text)
            if count != 1:
                raise ValueError(f'Ambiguous summary field: {path}')
        elif 'interface' in old:
            new, count = re.subn(r'(?m)^interface:[ \t]*$', lambda m: 'interface:\n  short_description: ' + value, text)
            if count != 1:
                raise ValueError(f'Unsupported interface formatting: {path}')
        else:
            new = text.rstrip() + ('\n' if text.strip() else '') + 'interface:\n  short_description: ' + value + '\n'
        parsed = yaml.safe_load(new)
        comparison = json.loads(json.dumps(parsed))
        comparison['interface'].pop('short_description')
        expected = json.loads(json.dumps(old))
        expected.setdefault('interface', {}).pop('short_description', None)
        if comparison != expected:
            raise ValueError(f'Unrelated metadata would change: {path}')
        updates.append((path, original, new.encode('utf-8')))
    return updates


def apply(plan, backup, dry_run=False):
    updates = prepare(plan)  # Validate every target before any write.
    if dry_run:
        return [str(path) for path, _, _ in updates]
    backup = Path(backup).expanduser().resolve()
    if backup.exists():
        raise ValueError('Backup destination already exists; choose a new directory')
    backup.mkdir(parents=True)
    (backup / 'files').mkdir()
    records = []
    for index, (path, original, new) in enumerate(updates):
        if original is not None:
            (backup / f'files/{index:04d}').write_bytes(original)
        records.append({'path': str(path), 'original': f'files/{index:04d}' if original is not None else None, 'after_sha256': digest(new)})
    (backup / 'manifest.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    for path, _, new in updates:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(new)
    return verify(plan)


def verify(plan):
    result = []
    for entry in plan:
        path = Path(entry['path']).expanduser().resolve() / 'agents/openai.yaml'
        try:
            ui = yaml.safe_load(path.read_text())
            actual = ui['interface']['short_description']
            ok = actual == entry['summary']
            result.append({'path': str(path), 'ok': ok, 'actual': actual})
        except (OSError, KeyError, TypeError, yaml.YAMLError) as error:
            result.append({'path': str(path), 'ok': False, 'error': str(error)})
    return result


def restore(backup, dry_run=False):
    backup = Path(backup).expanduser().resolve()
    records = json.loads((backup / 'manifest.json').read_text())
    for record in records:
        path = Path(record['path'])
        if not path.is_file() or path.is_symlink() or digest(path.read_bytes()) != record['after_sha256']:
            raise ValueError(f'Refusing to overwrite a later edit: {path}')
        if record['original']:
            saved = (backup / record['original']).resolve()
            if not saved.is_relative_to(backup) or not saved.is_file():
                raise ValueError('Invalid backup path')
    if not dry_run:
        for record in records:
            path = Path(record['path'])
            if record['original']:
                path.write_bytes((backup / record['original']).read_bytes())
            else:
                path.unlink()
    return {'restored': 0 if dry_run else len(records), 'dry_run': dry_run}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    sub = subs.add_parser('scan')
    sub.add_argument('--root', action='append', required=True)
    sub = subs.add_parser('apply')
    sub.add_argument('--plan', required=True)
    sub.add_argument('--backup', required=True)
    sub.add_argument('--dry-run', action='store_true')
    sub = subs.add_parser('verify')
    sub.add_argument('--plan', required=True)
    sub = subs.add_parser('restore')
    sub.add_argument('--backup', required=True)
    sub.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        if args.command == 'scan':
            result = scan(args.root)
        elif args.command == 'restore':
            result = restore(args.backup, args.dry_run)
        else:
            plan = json.loads(Path(args.plan).read_text())
            result = apply(plan, args.backup, args.dry_run) if args.command == 'apply' else verify(plan)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.command == 'verify' and not all(r['ok'] for r in result):
            return 1
    except (ValueError, OSError, KeyError, yaml.YAMLError) as error:
        parser.exit(2, str(error) + '\n')
    return 0

if __name__ == '__main__':
    sys.exit(main())
