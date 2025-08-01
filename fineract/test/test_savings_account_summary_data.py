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

from fineract_client.models.savings_account_summary_data import SavingsAccountSummaryData

class TestSavingsAccountSummaryData(unittest.TestCase):
    """SavingsAccountSummaryData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SavingsAccountSummaryData:
        """Test SavingsAccountSummaryData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SavingsAccountSummaryData`
        """
        model = SavingsAccountSummaryData()
        if include_optional:
            return SavingsAccountSummaryData(
                account_balance = 1.337,
                available_balance = 1.337,
                currency = fineract_client.models.currency_data.CurrencyData(
                    code = '', 
                    decimal_places = 56, 
                    display_label = '', 
                    display_symbol = '', 
                    in_multiples_of = 56, 
                    name = '', 
                    name_code = '', ),
                interest_not_posted = 1.337,
                interest_posted_till_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                last_interest_calculation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                prev_interest_posted_till_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                running_balance_on_interest_posting_till_date = 1.337,
                running_balance_on_pivot_date = 1.337,
                total_annual_fees = 1.337,
                total_deposits = 1.337,
                total_fee_charge = 1.337,
                total_interest_earned = 1.337,
                total_interest_posted = 1.337,
                total_overdraft_interest_derived = 1.337,
                total_penalty_charge = 1.337,
                total_withdrawal_fees = 1.337,
                total_withdrawals = 1.337,
                total_withhold_tax = 1.337
            )
        else:
            return SavingsAccountSummaryData(
        )
        """

    def testSavingsAccountSummaryData(self):
        """Test SavingsAccountSummaryData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
