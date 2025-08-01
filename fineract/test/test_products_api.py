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

from apis.products_api import ProductsApi


class TestProductsApi(unittest.TestCase):
    """ProductsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProductsApi()

    def tearDown(self) -> None:
        pass

    def test_create_product(self) -> None:
        """Test case for create_product

        Create a Share Product
        """
        pass

    def test_handle_commands3(self) -> None:
        """Test case for handle_commands3

        """
        pass

    def test_retrieve_all_products(self) -> None:
        """Test case for retrieve_all_products

        List Share Products
        """
        pass

    def test_retrieve_product(self) -> None:
        """Test case for retrieve_product

        Retrieve a Share Product
        """
        pass

    def test_retrieve_template13(self) -> None:
        """Test case for retrieve_template13

        """
        pass

    def test_update_product(self) -> None:
        """Test case for update_product

        Update a Share Product
        """
        pass


if __name__ == '__main__':
    unittest.main()
