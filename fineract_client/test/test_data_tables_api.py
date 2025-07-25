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

from fineract_client.api.data_tables_api import DataTablesApi


class TestDataTablesApi(unittest.TestCase):
    """DataTablesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataTablesApi()

    def tearDown(self) -> None:
        pass

    def test_advanced_query(self) -> None:
        """Test case for advanced_query

        Query Data Table values
        """
        pass

    def test_create_datatable(self) -> None:
        """Test case for create_datatable

        Create Data Table
        """
        pass

    def test_create_datatable_entry(self) -> None:
        """Test case for create_datatable_entry

        Create Entry in Data Table
        """
        pass

    def test_delete_datatable(self) -> None:
        """Test case for delete_datatable

        Delete Data Table
        """
        pass

    def test_delete_datatable_entries(self) -> None:
        """Test case for delete_datatable_entries

        Delete Entry(s) in Data Table
        """
        pass

    def test_delete_datatable_entry(self) -> None:
        """Test case for delete_datatable_entry

        Delete Entry in Datatable (One to Many)
        """
        pass

    def test_deregister_datatable(self) -> None:
        """Test case for deregister_datatable

        Deregister Data Table
        """
        pass

    def test_get_datatable(self) -> None:
        """Test case for get_datatable

        Retrieve Data Table Details
        """
        pass

    def test_get_datatable1(self) -> None:
        """Test case for get_datatable1

        Retrieve Entry(s) from Data Table
        """
        pass

    def test_get_datatable_many_entry(self) -> None:
        """Test case for get_datatable_many_entry

        """
        pass

    def test_get_datatables(self) -> None:
        """Test case for get_datatables

        List Data Tables
        """
        pass

    def test_query_values(self) -> None:
        """Test case for query_values

        Query Data Table values
        """
        pass

    def test_register_datatable(self) -> None:
        """Test case for register_datatable

        Register Data Table
        """
        pass

    def test_update_datatable(self) -> None:
        """Test case for update_datatable

        Update Data Table
        """
        pass

    def test_update_datatable_entry_one_to_many(self) -> None:
        """Test case for update_datatable_entry_one_to_many

        Update Entry in Data Table (One to Many)
        """
        pass

    def test_update_datatable_entry_oneto_one(self) -> None:
        """Test case for update_datatable_entry_oneto_one

        Update Entry in Data Table (One to One)
        """
        pass


if __name__ == '__main__':
    unittest.main()
