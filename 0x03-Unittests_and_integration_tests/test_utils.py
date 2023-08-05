#!/usr/bin/env python3
"""Parameterize a unit test """
import unittest
from parameterized import parameterized
from utils import access_nested_map


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
