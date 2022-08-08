#!/usr/bin/python3
"""This module defines unit tests for base.py"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Unit tests for base.py"""

    def test_init(self):
        """Initialize with no arguments"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_init_param(self):
        """INitialize with arguments"""
        b1 = Base(6)
        self.assertEqual(b1.id, 6)
        b2 = Base(25)
        self.assertEqual(b2.id, 25)
        b3 = Base(-1)
        self.assertEqual(b3.id, -1)
        b4 = Base(0)
        self.assertEqual(b4.id, 0)

    def test_init_mix(self):
        """Intialize with ID and without"""
        b1 = Base(2)
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 4)
