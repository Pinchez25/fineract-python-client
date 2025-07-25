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

from fineract_client.models.get_users_template_response import GetUsersTemplateResponse

class TestGetUsersTemplateResponse(unittest.TestCase):
    """GetUsersTemplateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUsersTemplateResponse:
        """Test GetUsersTemplateResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUsersTemplateResponse`
        """
        model = GetUsersTemplateResponse()
        if include_optional:
            return GetUsersTemplateResponse(
                allowed_offices = [
                    fineract_client.models.office_data.OfficeData(
                        date_format = '', 
                        external_id = fineract_client.models.external_id.ExternalId(
                            empty = True, 
                            value = '', ), 
                        hierarchy = '', 
                        id = 56, 
                        locale = '', 
                        name = '', 
                        name_decorated = '', 
                        opening_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        parent_id = 56, 
                        parent_name = '', 
                        row_index = 56, )
                    ],
                available_roles = [
                    fineract_client.models.role_data.RoleData(
                        id = 56, 
                        name = '', )
                    ],
                self_service_roles = [
                    fineract_client.models.role_data.RoleData(
                        id = 56, 
                        name = '', )
                    ]
            )
        else:
            return GetUsersTemplateResponse(
        )
        """

    def testGetUsersTemplateResponse(self):
        """Test GetUsersTemplateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
