# coding: utf-8

"""
    Apache Fineract REST API

    Apache Fineract is a secure, multi-tenanted microfinance platform. The goal of the Apache Fineract API is to empower developers to build apps on top of the Apache Fineract Platform. The https://cui.fineract.dev[reference app] (username: mifos, password: password) works on the same demo tenant as the interactive links in this documentation. Until we complete the new REST API documentation you still have the legacy documentation available https://fineract.apache.org/legacy-docs/apiLive.htm[here]. Please check https://fineract.apache.org/docs/current[the Fineract documentation] for more information.

    The version of the OpenAPI document: 1.11.0-SNAPSHOT
    Contact: dev@fineract.apache.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fineract_client.api.spmapi_look_up_table_api import SPMAPILookUpTableApi


class TestSPMAPILookUpTableApi(unittest.TestCase):
    """SPMAPILookUpTableApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SPMAPILookUpTableApi()

    def tearDown(self) -> None:
        pass

    def test_create_lookup_table(self) -> None:
        """Test case for create_lookup_table

        Create a Lookup Table entry
        """
        pass

    def test_fetch_lookup_tables(self) -> None:
        """Test case for fetch_lookup_tables

        List all Lookup Table entries
        """
        pass

    def test_find_lookup_table(self) -> None:
        """Test case for find_lookup_table

        Retrieve a Lookup Table entry
        """
        pass


if __name__ == '__main__':
    unittest.main()
