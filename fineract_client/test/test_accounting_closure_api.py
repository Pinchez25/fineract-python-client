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

from fineract_client.api.accounting_closure_api import AccountingClosureApi


class TestAccountingClosureApi(unittest.TestCase):
    """AccountingClosureApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountingClosureApi()

    def tearDown(self) -> None:
        pass

    def test_create_gl_closure(self) -> None:
        """Test case for create_gl_closure

        Create an Accounting Closure
        """
        pass

    def test_delete_gl_closure(self) -> None:
        """Test case for delete_gl_closure

        Delete an accounting closure
        """
        pass

    def test_retreive_closure(self) -> None:
        """Test case for retreive_closure

        Retrieve an Accounting Closure
        """
        pass

    def test_retrieve_all_closures(self) -> None:
        """Test case for retrieve_all_closures

        List Accounting closures
        """
        pass

    def test_update_gl_closure(self) -> None:
        """Test case for update_gl_closure

        Update an Accounting closure
        """
        pass


if __name__ == '__main__':
    unittest.main()
