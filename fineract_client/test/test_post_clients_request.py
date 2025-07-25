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

from fineract_client.models.post_clients_request import PostClientsRequest

class TestPostClientsRequest(unittest.TestCase):
    """PostClientsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostClientsRequest:
        """Test PostClientsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostClientsRequest`
        """
        model = PostClientsRequest()
        if include_optional:
            return PostClientsRequest(
                activation_date = '04 March 2009',
                active = True,
                address = [
                    fineract_client.models.post_clients_address_request.PostClientsAddressRequest(
                        address_line1 = 'Kandivali', 
                        address_line2 = 'plot47', 
                        address_line3 = 'charkop', 
                        address_type_id = 1, 
                        city = 'Mumbai', 
                        country_id = 802, 
                        is_active = True, 
                        postal_code = 400064, 
                        state_province_id = 800, 
                        street = 'Ipca', )
                    ],
                datatables = [
                    fineract_client.models.post_clients_datatable.PostClientsDatatable(
                        data = data, 
                        registered_table_name = 'Client Beneficiary information', )
                    ],
                date_format = 'dd MMMM yyyy',
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                email_address = 'test@test.com',
                external_id = '123',
                firstname = 'Client_FirstName',
                fullname = 'Client of group',
                group_id = 1,
                lastname = 'Client_LastName',
                legal_form_id = 1,
                locale = 'en',
                middlename = 'Client_MiddleName',
                mobile_no = '+353851239876',
                office_id = 1
            )
        else:
            return PostClientsRequest(
        )
        """

    def testPostClientsRequest(self):
        """Test PostClientsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
