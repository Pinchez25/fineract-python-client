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

from fineract_client.models.survey_data import SurveyData

class TestSurveyData(unittest.TestCase):
    """SurveyData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SurveyData:
        """Test SurveyData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SurveyData`
        """
        model = SurveyData()
        if include_optional:
            return SurveyData(
                component_datas = [
                    fineract_client.models.component_data.ComponentData(
                        description = '', 
                        id = 56, 
                        key = '', 
                        sequence_no = 56, 
                        text = '', )
                    ],
                country_code = '',
                description = '',
                id = 56,
                key = '',
                name = '',
                question_datas = [
                    fineract_client.models.question_data.QuestionData(
                        component_key = '', 
                        description = '', 
                        id = 56, 
                        key = '', 
                        response_datas = [
                            fineract_client.models.response_data.ResponseData(
                                id = 56, 
                                sequence_no = 56, 
                                text = '', 
                                value = 56, )
                            ], 
                        sequence_no = 56, 
                        text = '', )
                    ],
                valid_from = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                valid_to = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return SurveyData(
        )
        """

    def testSurveyData(self):
        """Test SurveyData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
