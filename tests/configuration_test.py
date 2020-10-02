from src.functions.configuration import get_configuration
import unittest
from src.functions import configuration

class TestSetup(unittest.TestCase):
    """Verify that the unittest framework is established and working.

    The tests here are not important except that if they fail it is an indication that something
    in the Python setup is not correct.
    """

    def test_no_config(self):
        with self.assertRaises(IOError):
            configuration.get_configuration(file_name = "does-not.exist")

    def test_invalid_config(self):
        with self.assertRaises(Exception):
            configuration.get_configuration(file_name = "test_bad_config.json")

    def test_returns_type(self):
        type, file = configuration.get_configuration(file_name = "test_good_config.json")
        self.assertEqual(type, "My favorite food")
        self.assertEqual(file, "test_data.csv")

if __name__ == '__main__':
    unittest.main()