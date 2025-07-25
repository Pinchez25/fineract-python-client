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

from apis.two_factor_api import TwoFactorApi


class TestTwoFactorApi(unittest.TestCase):
    """TwoFactorApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TwoFactorApi()

    def tearDown(self) -> None:
        pass

    def test_get_otp_delivery_methods(self) -> None:
        """Test case for get_otp_delivery_methods

        """
        pass

    def test_request_token(self) -> None:
        """Test case for request_token

        """
        pass

    def test_update_configuration2(self) -> None:
        """Test case for update_configuration2

        """
        pass

    def test_validate(self) -> None:
        """Test case for validate

        """
        pass


if __name__ == '__main__':
    unittest.main()
