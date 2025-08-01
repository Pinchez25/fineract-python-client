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

from fineract_client.models.get_accounts_summary import GetAccountsSummary

class TestGetAccountsSummary(unittest.TestCase):
    """GetAccountsSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccountsSummary:
        """Test GetAccountsSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccountsSummary`
        """
        model = GetAccountsSummary()
        if include_optional:
            return GetAccountsSummary(
                account_no = 2,
                currency = fineract_client.models.get_accounts_currency.GetAccountsCurrency(
                    code = 'USD', 
                    decimal_places = 2, 
                    display_label = 'US Dollar ($)', 
                    display_symbol = '$', 
                    in_multiples_of = 100, 
                    name = 'US Dollar', 
                    name_code = 'currency.USD', ),
                id = 2,
                product_id = 1,
                product_name = 'Conflux Share Product',
                status = fineract_client.models.get_accounts_status.GetAccountsStatus(
                    active = True, 
                    approved = False, 
                    closed = False, 
                    code = 'shareAccountStatusType.active', 
                    description = 'Active', 
                    id = 300, 
                    rejected = False, 
                    submitted_and_pending_approval = False, ),
                timeline = fineract_client.models.get_accounts_timeline.GetAccountsTimeline(
                    activated_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    approved_by_firstname = 'App', 
                    approved_by_lastname = 'Administrator', 
                    approved_by_username = 'mifos', 
                    approved_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    submitted_by_firstname = 'App', 
                    submitted_by_lastname = 'Administrator', 
                    submitted_by_username = 'mifos', 
                    submitted_on_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), ),
                total_approved_shares = 1,
                total_pending_for_approval_shares = 0
            )
        else:
            return GetAccountsSummary(
        )
        """

    def testGetAccountsSummary(self):
        """Test GetAccountsSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
