#!/usr/bin/python3
""" test module of add operationg"""
import unittest


def add(a, b):
    """add function for test case"""
    return (a + b)


class AddTestCase(unittest.TestCase):
    """Class representing a addition Test case"""

    def test_add_operation(self):
        self.assertEqual(2 + 2, 4)
        self.assertNotEqual(2 + 2, 5)

    def test_add_function(self):
        self.assertEqual(add(2, 2), 4)
        self.assertNotEqual(add(2, 2), 5)
