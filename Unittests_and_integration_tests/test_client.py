#!/usr/bin/env python3
""" Util testing module
"""

import unittest
import unittest.mock
from unittest.mock import PropertyMock
from parameterized import parameterized
import client
import utils


class TestGithubOrgClient(unittest.TestCase):
    """ tests for the GithubOrgClient class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, url, mock_json):
        """ test org method
        """
        test_request = client.GithubOrgClient(url)
        self.assertEqual(test_request.org, mock_json.return_value)
        mock_json.assert_called_once()

    def test_public_repos_url(self):
        """ test public_repos method
        """
        mock_name = 'client.GithubOrgClient._public_repos_url'
        with unittest.mock.patch(mock_name,
                                 new_callable=PropertyMock) as mock:
            mock.return_value = {'payload': 'success'}
            test_request = client.GithubOrgClient('test')
            self.assertEqual(test_request._public_repos_url, mock.return_value)

    @unittest.mock.patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ test public_repos method
        """
        mock_json.return_value = {'payload': 'success'}
        mock_name = 'client.GithubOrgClient._public_repos_url'
        with unittest.mock.patch(mock_name,
                                 new_callable=PropertyMock) as mock:
            mock.return_value = 'payload'
            test_request = client.GithubOrgClient('test')
            res = {'payload': 'success'}
            self.assertEqual(test_request.repos_payload, res)
            mock_json.assert_called_once()
            mock.assert_called_once()
