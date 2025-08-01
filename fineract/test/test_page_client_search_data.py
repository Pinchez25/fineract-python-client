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

from fineract_client.models.page_client_search_data import PageClientSearchData

class TestPageClientSearchData(unittest.TestCase):
    """PageClientSearchData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageClientSearchData:
        """Test PageClientSearchData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageClientSearchData`
        """
        model = PageClientSearchData()
        if include_optional:
            return PageClientSearchData(
                content = [
                    fineract_client.models.client_search_data.ClientSearchData(
                        account_number = '', 
                        activation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        display_name = '', 
                        external_id = fineract_client.models.external_id.ExternalId(
                            empty = True, 
                            value = '', ), 
                        id = 56, 
                        mobile_no = '', 
                        office_id = 56, 
                        office_name = '', 
                        status = fineract_client.models.enum_option_data.EnumOptionData(
                            code = '', 
                            id = 56, 
                            value = '', ), )
                    ],
                empty = True,
                first = True,
                last = True,
                number = 56,
                number_of_elements = 56,
                pageable = fineract_client.models.pageable.Pageable(
                    offset = 56, 
                    page_number = 56, 
                    page_size = 56, 
                    paged = True, 
                    sort = fineract_client.models.sort.Sort(
                        empty = True, 
                        sorted = True, 
                        unsorted = True, ), 
                    unpaged = True, ),
                size = 56,
                sort = fineract_client.models.sort.Sort(
                    empty = True, 
                    sorted = True, 
                    unsorted = True, ),
                total_elements = 56,
                total_pages = 56
            )
        else:
            return PageClientSearchData(
        )
        """

    def testPageClientSearchData(self):
        """Test PageClientSearchData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
