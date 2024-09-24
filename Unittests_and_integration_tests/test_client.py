#!/usr/bin/env python3
""" Util testing module
"""

import unittest
import unittest.mock
from parameterized import parameterized
import client


class TestGithubOrgClient(unittest.TestCase):
    """ tests for the GithubOrgClient class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, url, mock_json):
        test_request = client.GithubOrgClient(url)
        self.assertEqual(test_request.org, mock_json.return_value)
        mock_json.assert_called_once()
