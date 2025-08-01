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

from fineract_client.api.funds_api import FundsApi


class TestFundsApi(unittest.TestCase):
    """FundsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FundsApi()

    def tearDown(self) -> None:
        pass

    def test_create_fund(self) -> None:
        """Test case for create_fund

        Create a Fund
        """
        pass

    def test_retrieve_fund(self) -> None:
        """Test case for retrieve_fund

        Retrieve a Fund
        """
        pass

    def test_retrieve_funds(self) -> None:
        """Test case for retrieve_funds

        Retrieve Funds
        """
        pass

    def test_update_fund(self) -> None:
        """Test case for update_fund

        Update a Fund
        """
        pass


if __name__ == '__main__':
    unittest.main()
