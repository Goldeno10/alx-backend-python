#!/usr/bin/env python3
"""utils test cases module"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Test class for Access Nested Map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """access_nested_map()  test method"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """access_nested_map exception test"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

            # Check that the exception message is as expected
            self.assertEqual(
                str(context.exception),
                f"Key not found: {path[-1]}"
            )


class TestGetJson(unittest.TestCase):
    """Test class for get_json() function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """get_json() test method"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test class for the memoize function"""
    def test_memoize(self):
        """memoize() test method"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          "a_method",
                          return_value=42) as mocked_a_method:
            obj = TestClass()

            result_1 = obj.a_property
            result_2 = obj.a_property

            mocked_a_method.assert_called_once()

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)
