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

from fineract_client.models.interop_quote_request_data import InteropQuoteRequestData

class TestInteropQuoteRequestData(unittest.TestCase):
    """InteropQuoteRequestData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InteropQuoteRequestData:
        """Test InteropQuoteRequestData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InteropQuoteRequestData`
        """
        model = InteropQuoteRequestData()
        if include_optional:
            return InteropQuoteRequestData(
                account_id = '',
                amount = fineract_client.models.money_data.MoneyData(
                    amount = 1.337, 
                    currency = '', ),
                amount_type = 'SEND',
                expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expiration_local_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                extension_list = [
                    fineract_client.models.extension_data.ExtensionData(
                        key = '', 
                        value = '', )
                    ],
                fees = fineract_client.models.money_data.MoneyData(
                    amount = 1.337, 
                    currency = '', ),
                geo_code = fineract_client.models.geo_code_data.GeoCodeData(
                    latitude = '', 
                    longitude = '', ),
                note = '',
                quote_code = '',
                request_code = '',
                transaction_code = '',
                transaction_role = 'PAYER',
                transaction_type = fineract_client.models.interop_transaction_type_data.InteropTransactionTypeData(
                    initiator = 'PAYER', 
                    initiator_type = 'CONSUMER', 
                    scenario = 'DEPOSIT', 
                    sub_scenario = '', )
            )
        else:
            return InteropQuoteRequestData(
                account_id = '',
                amount = fineract_client.models.money_data.MoneyData(
                    amount = 1.337, 
                    currency = '', ),
                amount_type = 'SEND',
                quote_code = '',
                transaction_code = '',
                transaction_role = 'PAYER',
        )
        """

    def testInteropQuoteRequestData(self):
        """Test InteropQuoteRequestData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
