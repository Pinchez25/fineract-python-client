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

from fineract_client.models.retrieve_one_response import RetrieveOneResponse

class TestRetrieveOneResponse(unittest.TestCase):
    """RetrieveOneResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveOneResponse:
        """Test RetrieveOneResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveOneResponse`
        """
        model = RetrieveOneResponse()
        if include_optional:
            return RetrieveOneResponse(
                display_name = 'Doe, John',
                external_id = '17H',
                firstname = 'John',
                id = 1,
                is_active = False,
                is_loan_officer = True,
                joining_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                lastname = 'Doe',
                office_id = 1,
                office_name = 'Head Office'
            )
        else:
            return RetrieveOneResponse(
        )
        """

    def testRetrieveOneResponse(self):
        """Test RetrieveOneResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
