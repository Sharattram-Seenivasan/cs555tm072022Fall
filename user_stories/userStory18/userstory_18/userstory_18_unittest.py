import os
import unittest
from unittest.mock import patch
from userstory_18 import *
from helper_functions import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename1 = os.path.dirname(os.path.abspath(__file__)) + '/userstory_18_testdata1.ged'
        individuals, families = file_parser(filename1)
        output = output_data(individuals, families, filename1)
        no_sibling_marriage(individuals, families)
        mock_print.assert_called_with('ERROR: FAMILY: US18: F2 is a sibling marriage sharing the same parents!')

if __name__ == '__main__':
    unittest.main()