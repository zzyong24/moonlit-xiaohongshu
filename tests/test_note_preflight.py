import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class NotePreflightTests(unittest.TestCase):
    def check(self, text):
        spec = importlib.util.spec_from_file_location("preflight", ROOT / "scripts/preflight_note.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.validate_text(text)

    def test_rejects_external_url_even_inside_markdown(self):
        self.assertFalse(self.check("我把实际步骤记下来了：[项目](https://example.com/project)")["ok"])

    def test_rejects_www_and_html_link(self):
        for text in ['详情 www.example.com', '<a href="HTTPS://example.com">项目</a>']:
            with self.subTest(text=text):
                self.assertFalse(self.check(text)["ok"])

    def test_accepts_plain_product_name_and_local_reference(self):
        self.assertTrue(self.check("我在 CreatorOS 复现了字幕错位，三步找到了原因。配图路径留在素材清单。")["ok"])

    def test_long_text_is_blocked_without_echoing_copy(self):
        result = self.check("甲" * 501)
        self.assertFalse(result["ok"])
        self.assertEqual(result["characters"], 501)
        self.assertNotIn("甲", str(result))

if __name__ == "__main__":
    unittest.main()
