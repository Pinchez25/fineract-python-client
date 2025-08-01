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

from fineract_client.models.client_family_members_data import ClientFamilyMembersData

class TestClientFamilyMembersData(unittest.TestCase):
    """ClientFamilyMembersData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientFamilyMembersData:
        """Test ClientFamilyMembersData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientFamilyMembersData`
        """
        model = ClientFamilyMembersData()
        if include_optional:
            return ClientFamilyMembersData(
                age = 56,
                client_id = 56,
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                first_name = '',
                gender = '',
                gender_id = 56,
                gender_id_options = [
                    fineract_client.models.code_value_data.CodeValueData(
                        active = True, 
                        description = '', 
                        id = 56, 
                        mandatory = True, 
                        name = '', 
                        position = 56, )
                    ],
                id = 56,
                is_dependent = True,
                last_name = '',
                marital_status = '',
                marital_status_id = 56,
                marital_status_id_options = [
                    fineract_client.models.code_value_data.CodeValueData(
                        active = True, 
                        description = '', 
                        id = 56, 
                        mandatory = True, 
                        name = '', 
                        position = 56, )
                    ],
                middle_name = '',
                mobile_number = '',
                profession = '',
                profession_id = 56,
                profession_id_options = [
                    fineract_client.models.code_value_data.CodeValueData(
                        active = True, 
                        description = '', 
                        id = 56, 
                        mandatory = True, 
                        name = '', 
                        position = 56, )
                    ],
                qualification = '',
                relationship = '',
                relationship_id = 56,
                relationship_id_options = [
                    fineract_client.models.code_value_data.CodeValueData(
                        active = True, 
                        description = '', 
                        id = 56, 
                        mandatory = True, 
                        name = '', 
                        position = 56, )
                    ]
            )
        else:
            return ClientFamilyMembersData(
        )
        """

    def testClientFamilyMembersData(self):
        """Test ClientFamilyMembersData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
