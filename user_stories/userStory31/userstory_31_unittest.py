import os
import sys
import unittest
from unittest.mock import patch
from userstory_31 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data

class TestStringMethods(unittest.TestCase):

    @patch('builtins.print')
    def test_file_1(self, mock_print):
        filename = os.path.dirname(__file__) + '/../../test_data.ged'
        individuals, families = file_parser(filename)
        #output = output_data(individuals, families, filename)
        list_living_single(individuals, families)
        mock_print.assert_called_with("US30: The list of living people that are married: ['I1', 'I4', 'I8']")

if __name__ == '__main__':
    unittest.main()