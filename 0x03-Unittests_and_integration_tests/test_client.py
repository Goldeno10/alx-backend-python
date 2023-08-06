#!/usr/bin/env python3
"""client test cases module"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import *


class TestGithubOrgClient(unittest.TestCase):
    """GithubOrgClient test class"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """org() method test method"""
        # Mock the get_json response for org method
        mock_get_json.return_value = {
            "name": org_name,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Assert that the mocked get_json is called once
        # with the expected argument
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
            )

        # Assert that the result is correct
        self.assertEqual(
            result,
            {
                "name": org_name,
                "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
            }
        )
    
    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json):
        """public_repos_url() test method"""
        org_name = "testorg"
        repos_url = "https://api.github.com/orgs/testorg/repos"
        # Mock the get_json response for org method
        mock_get_json.return_value = {"name": org_name, "repos_url": repos_url}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Access the _public_repos_url property
        result = client._public_repos_url

        # Assert that the mocked get_json is called once with the expected argument
        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format(org=org_name))

        # Assert that the result is correct
        self.assertEqual(result, repos_url)
