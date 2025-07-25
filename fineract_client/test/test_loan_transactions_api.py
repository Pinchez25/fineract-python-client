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

from fineract_client.api.loan_transactions_api import LoanTransactionsApi


class TestLoanTransactionsApi(unittest.TestCase):
    """LoanTransactionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LoanTransactionsApi()

    def tearDown(self) -> None:
        pass

    def test_adjust_loan_transaction(self) -> None:
        """Test case for adjust_loan_transaction

        Adjust a Transaction
        """
        pass

    def test_adjust_loan_transaction1(self) -> None:
        """Test case for adjust_loan_transaction1

        Adjust a Transaction
        """
        pass

    def test_adjust_loan_transaction2(self) -> None:
        """Test case for adjust_loan_transaction2

        Adjust a Transaction
        """
        pass

    def test_adjust_loan_transaction3(self) -> None:
        """Test case for adjust_loan_transaction3

        Adjust a Transaction
        """
        pass

    def test_execute_loan_transaction(self) -> None:
        """Test case for execute_loan_transaction

        Significant Loan Transactions
        """
        pass

    def test_execute_loan_transaction1(self) -> None:
        """Test case for execute_loan_transaction1

        Significant Loan Transactions
        """
        pass

    def test_retrieve_transaction(self) -> None:
        """Test case for retrieve_transaction

        Retrieve a Transaction Details
        """
        pass

    def test_retrieve_transaction_by_loan_external_id_and_transaction_external_id(self) -> None:
        """Test case for retrieve_transaction_by_loan_external_id_and_transaction_external_id

        Retrieve a Transaction Details
        """
        pass

    def test_retrieve_transaction_by_loan_external_id_and_transaction_id(self) -> None:
        """Test case for retrieve_transaction_by_loan_external_id_and_transaction_id

        Retrieve a Transaction Details
        """
        pass

    def test_retrieve_transaction_by_transaction_external_id(self) -> None:
        """Test case for retrieve_transaction_by_transaction_external_id

        Retrieve a Transaction Details
        """
        pass

    def test_retrieve_transaction_template(self) -> None:
        """Test case for retrieve_transaction_template

        Retrieve Loan Transaction Template
        """
        pass

    def test_retrieve_transaction_template1(self) -> None:
        """Test case for retrieve_transaction_template1

        Retrieve Loan Transaction Template
        """
        pass

    def test_undo_waive_charge(self) -> None:
        """Test case for undo_waive_charge

        Undo a Waive Charge Transaction
        """
        pass

    def test_undo_waive_charge1(self) -> None:
        """Test case for undo_waive_charge1

        Undo a Waive Charge Transaction
        """
        pass

    def test_undo_waive_charge2(self) -> None:
        """Test case for undo_waive_charge2

        Undo a Waive Charge Transaction
        """
        pass

    def test_undo_waive_charge3(self) -> None:
        """Test case for undo_waive_charge3

        Undo a Waive Charge Transaction
        """
        pass


if __name__ == '__main__':
    unittest.main()
