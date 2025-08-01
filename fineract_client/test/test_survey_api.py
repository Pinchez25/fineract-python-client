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

from fineract_client.api.survey_api import SurveyApi


class TestSurveyApi(unittest.TestCase):
    """SurveyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SurveyApi()

    def tearDown(self) -> None:
        pass

    def test_create_datatable_entry1(self) -> None:
        """Test case for create_datatable_entry1

        Create an entry in the survey table
        """
        pass

    def test_delete_datatable_entries1(self) -> None:
        """Test case for delete_datatable_entries1

        """
        pass

    def test_get_client_survey_overview(self) -> None:
        """Test case for get_client_survey_overview

        """
        pass

    def test_get_survey_entry(self) -> None:
        """Test case for get_survey_entry

        """
        pass

    def test_register(self) -> None:
        """Test case for register

        """
        pass

    def test_retrieve_survey(self) -> None:
        """Test case for retrieve_survey

        Retrieve survey
        """
        pass

    def test_retrieve_surveys(self) -> None:
        """Test case for retrieve_surveys

        Retrieve surveys
        """
        pass


if __name__ == '__main__':
    unittest.main()
