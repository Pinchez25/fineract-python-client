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

from apis.loan_collateral_management_api import LoanCollateralManagementApi


class TestLoanCollateralManagementApi(unittest.TestCase):
    """LoanCollateralManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LoanCollateralManagementApi()

    def tearDown(self) -> None:
        pass

    def test_delete_loan_collateral(self) -> None:
        """Test case for delete_loan_collateral

        Delete Loan Collateral
        """
        pass

    def test_get_loan_collateral(self) -> None:
        """Test case for get_loan_collateral

        Get Loan Collateral Details
        """
        pass


if __name__ == '__main__':
    unittest.main()
