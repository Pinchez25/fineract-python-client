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

from apis.payment_type_api import PaymentTypeApi


class TestPaymentTypeApi(unittest.TestCase):
    """PaymentTypeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PaymentTypeApi()

    def tearDown(self) -> None:
        pass

    def test_create_payment_type(self) -> None:
        """Test case for create_payment_type

        Create a Payment Type
        """
        pass

    def test_delete_code1(self) -> None:
        """Test case for delete_code1

        Delete a Payment Type
        """
        pass

    def test_get_all_payment_types(self) -> None:
        """Test case for get_all_payment_types

        Retrieve all Payment Types
        """
        pass

    def test_retrieve_one_payment_type(self) -> None:
        """Test case for retrieve_one_payment_type

        Retrieve a Payment Type
        """
        pass

    def test_update_payment_type(self) -> None:
        """Test case for update_payment_type

        Update a Payment Type
        """
        pass


if __name__ == '__main__':
    unittest.main()
