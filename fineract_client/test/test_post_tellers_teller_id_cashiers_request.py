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

from fineract_client.models.post_tellers_teller_id_cashiers_request import PostTellersTellerIdCashiersRequest

class TestPostTellersTellerIdCashiersRequest(unittest.TestCase):
    """PostTellersTellerIdCashiersRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostTellersTellerIdCashiersRequest:
        """Test PostTellersTellerIdCashiersRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostTellersTellerIdCashiersRequest`
        """
        model = PostTellersTellerIdCashiersRequest()
        if include_optional:
            return PostTellersTellerIdCashiersRequest(
                date_format = 'dd-MM-yyyy',
                description = 'teller cash handling',
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                is_full_day = True,
                locale = 'en',
                staff_id = 3,
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return PostTellersTellerIdCashiersRequest(
        )
        """

    def testPostTellersTellerIdCashiersRequest(self):
        """Test PostTellersTellerIdCashiersRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
