#!/usr/bin/python
# -*- coding: utf-8 -*-

# run with pytest

import unittest
from peatmoss_sentence_test import side

class Test(unittest.TestCase):
    def test_side(self):
        self.assertEqual(side.pure_import(), 0)

if __name__ == '__main__':
    unittest.main()