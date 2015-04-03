#!/usr/bin/env python
"""
Unit test suite for the CESM diagnostics wrapper scripts

"""

from __future__ import print_function

import os
import unittest

from diag_utils import diagUtilsLib

class test_checkFile(unittest.TestCase):
    def setUp(self):
        self.test_data = []

    def tearDown(self):
        pass

    def test_defaultFile(self):
        """ test to see if a known file can be read
        """
        found = diagUtilsLib.checkFile("./test_checkXMLvar.py", "read")
        self.assertTrue(found)

    def test_invalidFile(self):
        """ test to see if invalid file raises an error
        """
        self.assertRaises(diagUtilsLib.checkFile("blah", "write"))

if __name__ == '__main__':
    unittest.main()
