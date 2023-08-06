#!/usr/bin/env python3
"""client test cases module"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import PropertyMock, patch
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
    
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        org_name = "testorg"
        repos_url = "https://api.github.com/orgs/testorg/repos"
        mock_repo = [{"name": "repo1"}, {"name": "repo2"}]
        # Mock the get_json response for org method and repos_payload method
        mock_get_json.side_effect = [mock_repo, mock_repo]

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Use patch as a context manager to mock _public_repos_url property
        with patch.object(client, '_public_repos_url', new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = repos_url

            # Call the public_repos method
            result = client.public_repos()

            # Assert that the mocked _public_repos_url property is called once
            mock_repos_url.assert_called_once()

        # Assert that the mocked get_json is called once with the expected argument
        mock_get_json.assert_called_once_with(repos_url)

        # Assert that the result is correct
        self.assertEqual(result, ["repo1", "repo2"])

    
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """has_license() methodd test method"""
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("testorg")

        # Call the has_license method
        result = client.has_license(repo, license_key)

        # Assert that the result is correct
        self.assertEqual(result, expected_result)

@parameterized_class('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos')
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        # Set up mock for requests.get(url).json() side_effect
        self.mock_get.side_effect = [
            # Mock the response for org method
            type('Response', (object,), {'json': lambda: self.org_payload}),
            # Mock the response for repos_payload method
            type('Response', (object,), {'json': lambda: self.repos_payload}),
        ]

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("testorg")

        # Call the public_repos method
        result = client.public_repos()

        # Assert that the mocked requests.get is called with the expected argument
        self.mock_get.assert_called_with(self.org_payload["repos_url"])

        # Assert that the result is correct
        self.assertEqual(result, self.expected_repos)