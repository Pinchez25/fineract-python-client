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

from fineract_client.api.savings_account_transactions_api import SavingsAccountTransactionsApi


class TestSavingsAccountTransactionsApi(unittest.TestCase):
    """SavingsAccountTransactionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SavingsAccountTransactionsApi()

    def tearDown(self) -> None:
        pass

    def test_adjust_transaction1(self) -> None:
        """Test case for adjust_transaction1

        Undo/Reverse/Modify/Release Amount transaction API
        """
        pass

    def test_advanced_query1(self) -> None:
        """Test case for advanced_query1

        Advanced search Savings Account Transactions
        """
        pass

    def test_retrieve_one24(self) -> None:
        """Test case for retrieve_one24

        """
        pass

    def test_retrieve_template19(self) -> None:
        """Test case for retrieve_template19

        """
        pass

    def test_search_transactions(self) -> None:
        """Test case for search_transactions

        Search Savings Account Transactions
        """
        pass

    def test_transaction2(self) -> None:
        """Test case for transaction2

        """
        pass


if __name__ == '__main__':
    unittest.main()
