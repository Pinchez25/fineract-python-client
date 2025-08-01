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

from fineract_client.models.interop_transactions_data import InteropTransactionsData

class TestInteropTransactionsData(unittest.TestCase):
    """InteropTransactionsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InteropTransactionsData:
        """Test InteropTransactionsData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InteropTransactionsData`
        """
        model = InteropTransactionsData()
        if include_optional:
            return InteropTransactionsData(
                changes = {
                    'key' : None
                    },
                client_id = 56,
                command_id = 56,
                credit_bureau_report_data = {
                    'key' : None
                    },
                glim_id = 56,
                group_id = 56,
                gsim_id = 56,
                loan_id = 56,
                office_id = 56,
                product_id = 56,
                resource_external_id = fineract_client.models.external_id.ExternalId(
                    empty = True, 
                    value = '', ),
                resource_id = 56,
                resource_identifier = '',
                rollback_transaction = True,
                savings_id = 56,
                sub_resource_external_id = fineract_client.models.external_id.ExternalId(
                    empty = True, 
                    value = '', ),
                sub_resource_id = 56,
                transaction_id = '',
                transactions = [
                    fineract_client.models.interop_transaction_data.InteropTransactionData(
                        account_balance = 1.337, 
                        account_id = '', 
                        amount = 1.337, 
                        booking_date_time = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        changes = {
                            'key' : None
                            }, 
                        charge_amount = 1.337, 
                        client_id = 56, 
                        command_id = 56, 
                        credit_bureau_report_data = {
                            'key' : None
                            }, 
                        currency = '', 
                        glim_id = 56, 
                        group_id = 56, 
                        gsim_id = 56, 
                        loan_id = 56, 
                        note = '', 
                        office_id = 56, 
                        product_id = 56, 
                        resource_external_id = fineract_client.models.external_id.ExternalId(
                            empty = True, 
                            value = '', ), 
                        resource_id = 56, 
                        resource_identifier = '', 
                        rollback_transaction = True, 
                        saving_transaction_id = '', 
                        savings_id = 56, 
                        sub_resource_external_id = fineract_client.models.external_id.ExternalId(
                            empty = True, 
                            value = '', ), 
                        sub_resource_id = 56, 
                        transaction_id = '', 
                        transaction_type = 'INVALID', 
                        value_date_time = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                    ]
            )
        else:
            return InteropTransactionsData(
        )
        """

    def testInteropTransactionsData(self):
        """Test InteropTransactionsData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
