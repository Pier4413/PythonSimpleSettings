import unittest
import os
import tempfile
from configparser import ConfigParser

from .. import Settings  # Replace with actual import path


class TestSettings(unittest.TestCase):
    def test_all_settings_behaviors(self):
        # Prepare temp file
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w+", encoding="utf-8")
        temp_file.write(
            "[General]\n"
            "username = testuser\n"
            "timeout = 30\n"
            "debug = yes\n"
            "rate = 1.5\n"
        )
        temp_file.close()

        try:
            # Reset singleton
            Settings.__instance = None

            # Singleton creation
            settings = Settings.get_instance()
            settings.load_settings(temp_file.name)
            self.assertEqual(settings, Settings.get_instance(), "Singleton instance mismatch")

            # Test get (existing and default)
            self.assertEqual(Settings.get("General", "username", "default"), "testuser", "get() failed for existing key")
            self.assertEqual(Settings.get("General", "nonexistent", "default"), "default", "get() failed for default")

            # Test getint, getboolean, getfloat
            self.assertEqual(Settings.getint("General", "timeout", 0), 30, "getint() failed")
            self.assertTrue(Settings.getboolean("General", "debug", False), "getboolean() failed")
            self.assertAlmostEqual(Settings.getfloat("General", "rate", 0.0), 1.5, msg="getfloat() failed")

            # Test set and write
            Settings.set("General", "newkey", "newvalue")
            Settings.write()
            config = ConfigParser()
            config.read(temp_file.name, encoding="utf8")
            self.assertTrue(config.has_option("General", "newkey"), "set() or write() failed")
            self.assertEqual(config.get("General", "newkey"), "newvalue", "Incorrect written value")

            # Double instantiation should raise
            with self.assertRaises(Exception, msg="Singleton did not prevent second instance"):
                Settings()

        finally:
            os.remove(temp_file.name)
            Settings.__instance = None
            
if __name__ == "__main__":
    unittest.main()
