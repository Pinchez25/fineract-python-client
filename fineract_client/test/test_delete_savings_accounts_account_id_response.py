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

from fineract_client.models.delete_savings_accounts_account_id_response import DeleteSavingsAccountsAccountIdResponse

class TestDeleteSavingsAccountsAccountIdResponse(unittest.TestCase):
    """DeleteSavingsAccountsAccountIdResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteSavingsAccountsAccountIdResponse:
        """Test DeleteSavingsAccountsAccountIdResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteSavingsAccountsAccountIdResponse`
        """
        model = DeleteSavingsAccountsAccountIdResponse()
        if include_optional:
            return DeleteSavingsAccountsAccountIdResponse(
                client_id = 1,
                office_id = 1,
                resource_id = 1
            )
        else:
            return DeleteSavingsAccountsAccountIdResponse(
        )
        """

    def testDeleteSavingsAccountsAccountIdResponse(self):
        """Test DeleteSavingsAccountsAccountIdResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
