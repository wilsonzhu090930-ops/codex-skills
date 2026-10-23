import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).parents[1] / 'skills/skill-summary-zh/scripts/localize.py'

class LocalizerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.skill = self.root / 'example'
        self.skill.mkdir()
        self.text = '---\nname: example\ndescription: Use for reviewing code.\nmetadata:\n  version: "1"\n---\n\n# Example\nKeep all instructions.\n'
        (self.skill / 'SKILL.md').write_text(self.text)
        spec = importlib.util.spec_from_file_location('localize', SCRIPT)
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)
        self.plan = [{'path': str(self.skill), 'summary': '按需求和规范审查代码改动'}]

    def test_adds_ui_without_changing_skill(self):
        self.mod.apply(self.plan, self.root / 'backup', False)
        self.assertEqual((self.skill / 'SKILL.md').read_text(), self.text)
        self.assertTrue(self.mod.verify(self.plan)[0]['ok'])

    def test_preserves_policy_and_prompts(self):
        ui = self.skill / 'agents/openai.yaml'
        ui.parent.mkdir()
        original = 'interface:\n  display_name: "Example"\n  short_description: "Review code"\n  default_prompt: "Review this"\npolicy:\n  allow_implicit_invocation: false\n'
        ui.write_text(original)
        self.mod.apply(self.plan, self.root / 'backup', False)
        import yaml
        before, after = yaml.safe_load(original), yaml.safe_load(ui.read_text())
        before['interface'].pop('short_description')
        after['interface'].pop('short_description')
        self.assertEqual(before, after)
        self.assertEqual((self.root / 'backup/files/0000').read_text(), original)

    def test_dry_run_has_no_side_effect(self):
        self.mod.apply(self.plan, self.root / 'backup', True)
        self.assertFalse((self.skill / 'agents').exists())
        self.assertFalse((self.root / 'backup').exists())

    def test_rejects_english_or_multiline(self):
        for value in ['Review code', '检查代码\n并更新', '检' * 29]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.mod.apply([{'path': str(self.skill), 'summary': value}], self.root / 'backup', False)
        self.assertFalse((self.skill / 'agents').exists())

    def test_invalid_later_item_leaves_earlier_untouched(self):
        plan = self.plan + [{'path': str(self.root / 'missing'), 'summary': '检查并翻译技能列表说明'}]
        with self.assertRaises(ValueError):
            self.mod.apply(plan, self.root / 'backup', False)
        self.assertFalse((self.skill / 'agents').exists())

    def test_detects_changed_result(self):
        self.mod.apply(self.plan, self.root / 'backup', False)
        (self.skill / 'agents/openai.yaml').write_text('interface:\n  short_description: "Wrong"\n')
        self.assertFalse(self.mod.verify(self.plan)[0]['ok'])

    def test_scan_does_not_recurse_into_unrelated_folders(self):
        nested = self.root / 'unrelated/deep'
        nested.mkdir(parents=True)
        (nested / 'SKILL.md').write_text(self.text)
        result = self.mod.scan([self.root])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'example')

    def test_restore_refuses_to_overwrite_later_edits(self):
        self.mod.apply(self.plan, self.root / 'backup', False)
        (self.skill / 'agents/openai.yaml').write_text('interface:\n  short_description: "后来手动编辑过的说明"\n')
        with self.assertRaises(ValueError):
            self.mod.restore(self.root / 'backup', False)

    def test_restore_removes_only_generated_file(self):
        self.mod.apply(self.plan, self.root / 'backup', False)
        self.mod.restore(self.root / 'backup', False)
        self.assertFalse((self.skill / 'agents/openai.yaml').exists())
        self.assertEqual((self.skill / 'SKILL.md').read_text(), self.text)

if __name__ == '__main__':
    unittest.main()
