#!/usr/bin/env python3
""" Util testing module
"""

import unittest
import unittest.mock
from parameterized import parameterized
import utils


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
        self.assertEqual(utils.access_nested_map(nest, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nest, path):
        """test unsuccessful execution of access_nested_map()"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nest, path)


class TestGetJson(unittest.TestCase):
    """ tests for the get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch('utils.requests')
    def test_get_json(self, url, payload, mock_requests):
        mock_requests.get.return_value.json.return_value = payload
        self.assertEqual(utils.get_json(url), payload)
        mock_requests.get.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ tests for the memoize decorator
    """

    def test_memoize(self):
        """ memoize test method
        """

        class TestClass:
            """ test class for memoize tests
            """

            def a_method(self):
                """test method"""
                return 42

            @utils.memoize
            def a_property(self):
                """ getter property with memoization
                """
                return self.a_method()

        with unittest.mock.patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mock_method.assert_called_once()
