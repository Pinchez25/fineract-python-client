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

from fineract_client.models.get_clients_loan_accounts import GetClientsLoanAccounts

class TestGetClientsLoanAccounts(unittest.TestCase):
    """GetClientsLoanAccounts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetClientsLoanAccounts:
        """Test GetClientsLoanAccounts
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetClientsLoanAccounts`
        """
        model = GetClientsLoanAccounts()
        if include_optional:
            return GetClientsLoanAccounts(
                account_no = '000000001',
                currency = fineract_client.models.get_clients_loans_accounts_currency.GetClientsLoansAccountsCurrency(
                    code = 'USD', 
                    decimal_places = 2, 
                    display_label = 'US Dollar ($)', 
                    display_symbol = '$', 
                    name = 'US Dollar', 
                    name_code = 'currency.USD', ),
                external_id = '456',
                id = 1,
                loan_cycle = 1,
                loan_type = fineract_client.models.get_clients_loan_accounts_type.GetClientsLoanAccountsType(
                    code = 'loanType.individual', 
                    description = 'Individual', 
                    id = 1, ),
                product_id = 1,
                product_name = 'TestOne',
                short_product_name = 'OP',
                status = fineract_client.models.get_clients_loan_accounts_status.GetClientsLoanAccountsStatus(
                    active = True, 
                    closed = False, 
                    closed_obligations_met = False, 
                    closed_rescheduled = False, 
                    closed_written_off = False, 
                    code = 'loanStatusType.active', 
                    description = 'Active', 
                    id = 300, 
                    overpaid = False, 
                    pending_approval = False, 
                    waiting_for_disbursal = False, )
            )
        else:
            return GetClientsLoanAccounts(
        )
        """

    def testGetClientsLoanAccounts(self):
        """Test GetClientsLoanAccounts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
