import unittest
from src.functions import datafile

class test_fileio(unittest.TestCase):
    """ Verify that file functions are working

    """

    def test_nofile(self):

        data = datafile.get_data("./data/file_does_not.exist")
        self.assertEqual(len(data), 0)