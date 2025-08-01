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

from fineract_client.api.recurring_deposit_account_api import RecurringDepositAccountApi


class TestRecurringDepositAccountApi(unittest.TestCase):
    """RecurringDepositAccountApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RecurringDepositAccountApi()

    def tearDown(self) -> None:
        pass

    def test_account_closure_template1(self) -> None:
        """Test case for account_closure_template1

        """
        pass

    def test_delete17(self) -> None:
        """Test case for delete17

        Delete a recurring deposit application
        """
        pass

    def test_get_recurring_deposit_template(self) -> None:
        """Test case for get_recurring_deposit_template

        """
        pass

    def test_get_recurring_deposit_transaction_template(self) -> None:
        """Test case for get_recurring_deposit_transaction_template

        """
        pass

    def test_handle_commands5(self) -> None:
        """Test case for handle_commands5

        Approve recurring deposit application | Undo approval recurring deposit application | Reject recurring deposit application | Withdraw recurring deposit application | Activate a recurring deposit account | Update the recommended deposit amount for a recurring deposit account | Close a recurring deposit account | Premature Close a recurring deposit account | Calculate Premature amount on Recurring deposit account | Calculate Interest on recurring Deposit Account | Post Interest on recurring Deposit Account
        """
        pass

    def test_post_recurring_deposit_template(self) -> None:
        """Test case for post_recurring_deposit_template

        """
        pass

    def test_post_recurring_deposit_transactions_template(self) -> None:
        """Test case for post_recurring_deposit_transactions_template

        """
        pass

    def test_retrieve_all31(self) -> None:
        """Test case for retrieve_all31

        List Recurring deposit applications/accounts
        """
        pass

    def test_retrieve_one22(self) -> None:
        """Test case for retrieve_one22

        Retrieve a recurring deposit application/account
        """
        pass

    def test_submit_application1(self) -> None:
        """Test case for submit_application1

        Submit new recurring deposit application
        """
        pass

    def test_template13(self) -> None:
        """Test case for template13

        Retrieve recurring Deposit Account Template
        """
        pass

    def test_update18(self) -> None:
        """Test case for update18

        Modify a recurring deposit application
        """
        pass


if __name__ == '__main__':
    unittest.main()
