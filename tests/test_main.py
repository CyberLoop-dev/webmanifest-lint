import unittest
from main import lint


class ManifestTests(unittest.TestCase):
    def test_valid_manifest(self):
        data = {
            "name":"Sample App", "start_url":"/app/home",
            "scope":"/app/", "display":"standalone",
            "icons":[{"src":"/icons/app.png","sizes":"192x192"}]
        }
        self.assertEqual(lint(data), [])

    def test_detects_scope_mismatch(self):
        data = {"name":"Sample", "start_url":"/outside", "scope":"/app/"}
        self.assertTrue(any("outside the declared scope" in m for _, m in lint(data)))

    def test_requires_a_name(self):
        self.assertTrue(any("provide name" in m for _, m in lint({})))

    def test_invalid_icon_sizes_do_not_crash(self):
        issues = lint({"name":"Sample","icons":[{"src":"/icon.png","sizes":["192x192"]}]})
        self.assertTrue(any("sizes must be a string" in message for _, message in issues))


if __name__ == "__main__":
    unittest.main()
