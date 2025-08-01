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

from fineract_client.models.loan_product_related_detail import LoanProductRelatedDetail

class TestLoanProductRelatedDetail(unittest.TestCase):
    """LoanProductRelatedDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoanProductRelatedDetail:
        """Test LoanProductRelatedDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoanProductRelatedDetail`
        """
        model = LoanProductRelatedDetail()
        if include_optional:
            return LoanProductRelatedDetail(
                allow_partial_period_interest_calcualtion = True,
                amortization_method = 'EQUAL_PRINCIPAL',
                annual_nominal_interest_rate = 1.337,
                currency = fineract_client.models.monetary_currency.MonetaryCurrency(
                    code = '', 
                    currency_in_multiples_of = 56, 
                    digits_after_decimal = 56, ),
                days_in_month_type = 56,
                days_in_year_type = 56,
                disbursed_amount_percentage_for_down_payment = 1.337,
                enable_accrual_activity_posting = True,
                enable_auto_repayment_for_down_payment = True,
                enable_down_payment = True,
                equal_amortization = True,
                fixed_length = 56,
                grace_on_arrears_ageing = 56,
                grace_on_interest_charged = 56,
                grace_on_interest_payment = 56,
                grace_on_principal_payment = 56,
                in_arrears_tolerance = fineract_client.models.money.Money(
                    amount = 1.337, 
                    amount_defaulted_to_null_if_zero = 1.337, 
                    currency = fineract_client.models.monetary_currency.MonetaryCurrency(
                        code = '', 
                        currency_in_multiples_of = 56, 
                        digits_after_decimal = 56, ), 
                    currency_code = '', 
                    currency_digits_after_decimal = 56, 
                    currency_in_multiples_of = 56, 
                    greater_than_zero = True, 
                    less_than_zero = True, 
                    zero = True, ),
                interest_calculation_period_method = 'DAILY',
                interest_method = 'DECLINING_BALANCE',
                interest_period_frequency_type = 'DAYS',
                interest_recalculation_enabled = True,
                loan_schedule_processing_type = 'HORIZONTAL',
                loan_schedule_type = 'CUMULATIVE',
                nominal_interest_rate_per_period = 1.337,
                number_of_repayments = 56,
                principal = fineract_client.models.money.Money(
                    amount = 1.337, 
                    amount_defaulted_to_null_if_zero = 1.337, 
                    currency = fineract_client.models.monetary_currency.MonetaryCurrency(
                        code = '', 
                        currency_in_multiples_of = 56, 
                        digits_after_decimal = 56, ), 
                    currency_code = '', 
                    currency_digits_after_decimal = 56, 
                    currency_in_multiples_of = 56, 
                    greater_than_zero = True, 
                    less_than_zero = True, 
                    zero = True, ),
                recurring_moratorium_on_principal_periods = 56,
                repay_every = 56,
                repayment_period_frequency_type = 'DAYS',
                supported_interest_refund_types = [
                    'MERCHANT_ISSUED_REFUND'
                    ]
            )
        else:
            return LoanProductRelatedDetail(
        )
        """

    def testLoanProductRelatedDetail(self):
        """Test LoanProductRelatedDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
