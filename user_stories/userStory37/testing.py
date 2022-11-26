import os
import sys
import unittest
from unittest.mock import patch
from userstory_37 import *
sys.path.append('')
from gedcom_helper import file_parser, output_data


filename = os.path.dirname(__file__) + '/../../test_data.ged'
individuals, families = file_parser(filename)
output = output_data(individuals, families, filename)
list_recent_survivors(individuals, families)
#mock_print.assert_called_with("US30: The list of living people that are married: ['I2', 'I3', 'I5', 'I6', 'I7']")