#!/usr/bin/python
# -*- coding: utf-8 -*-

# run with pytest

import unittest
from py_test_pack import main

class Test(unittest.TestCase):
    def test_main_one(self):
        self.assertEqual(main.regex("cat"), True)

    def test_main_two(self):
        self.assertEqual(main.regex("“hello”"), False)

    def test_main_three(self):
        self.assertEqual(main.sentence(), 0)

if __name__ == '__main__':
    unittest.main()