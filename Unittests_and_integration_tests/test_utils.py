#!/usr/bin/env python3
""" Util testing module
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """ test cases for the access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nest, path, expected):
        """test successful execution of access_nested_map()"""
        self.assertEqual(access_nested_map(nest, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nest, path):
        """test unsuccessful execution of access_nested_map()"""
        with self.assertRaises(KeyError):
            access_nested_map(nest, path)
