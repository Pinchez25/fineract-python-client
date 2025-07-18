# coding: utf-8

"""
    Apache Fineract REST API

    Apache Fineract is a secure, multi-tenanted microfinance platform. The goal of the Apache Fineract API is to empower developers to build apps on top of the Apache Fineract Platform. The https://cui.fineract.dev[reference app] (username: mifos, password: password) works on the same demo tenant as the interactive links in this documentation. Until we complete the new REST API documentation you still have the legacy documentation available https://fineract.apache.org/legacy-docs/apiLive.htm[here]. Please check https://fineract.apache.org/docs/current[the Fineract documentation] for more information.

    The version of the OpenAPI document: 1.11.0-SNAPSHOT
    Contact: dev@fineract.apache.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from fineract_client.models.get_savings_currency import GetSavingsCurrency
from fineract_client.models.get_savings_products_accounting_mappings import GetSavingsProductsAccountingMappings
from fineract_client.models.get_savings_products_accounting_rule import GetSavingsProductsAccountingRule
from fineract_client.models.get_savings_products_fee_to_income_account_mappings import GetSavingsProductsFeeToIncomeAccountMappings
from fineract_client.models.get_savings_products_interest_calculation_days_in_year_type import GetSavingsProductsInterestCalculationDaysInYearType
from fineract_client.models.get_savings_products_interest_calculation_type import GetSavingsProductsInterestCalculationType
from fineract_client.models.get_savings_products_interest_compounding_period_type import GetSavingsProductsInterestCompoundingPeriodType
from fineract_client.models.get_savings_products_interest_posting_period_type import GetSavingsProductsInterestPostingPeriodType
from fineract_client.models.get_savings_products_payment_channel_to_fund_source_mappings import GetSavingsProductsPaymentChannelToFundSourceMappings
from fineract_client.models.get_savings_products_penalty_to_income_account_mappings import GetSavingsProductsPenaltyToIncomeAccountMappings
from typing import Optional, Set
from typing_extensions import Self

class GetSavingsProductsProductIdResponse(BaseModel):
    """
    GetSavingsProductsProductIdResponse
    """ # noqa: E501
    accounting_mappings: Optional[GetSavingsProductsAccountingMappings] = Field(default=None, alias="accountingMappings")
    accounting_rule: Optional[GetSavingsProductsAccountingRule] = Field(default=None, alias="accountingRule")
    charges: Optional[List[StrictInt]] = None
    currency: Optional[GetSavingsCurrency] = None
    description: Optional[StrictStr] = None
    fee_to_income_account_mappings: Optional[List[GetSavingsProductsFeeToIncomeAccountMappings]] = Field(default=None, alias="feeToIncomeAccountMappings")
    id: Optional[StrictInt] = None
    interest_calculation_days_in_year_type: Optional[GetSavingsProductsInterestCalculationDaysInYearType] = Field(default=None, alias="interestCalculationDaysInYearType")
    interest_calculation_type: Optional[GetSavingsProductsInterestCalculationType] = Field(default=None, alias="interestCalculationType")
    interest_compounding_period_type: Optional[GetSavingsProductsInterestCompoundingPeriodType] = Field(default=None, alias="interestCompoundingPeriodType")
    interest_posting_period_type: Optional[GetSavingsProductsInterestPostingPeriodType] = Field(default=None, alias="interestPostingPeriodType")
    name: Optional[StrictStr] = None
    nominal_annual_interest_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="nominalAnnualInterestRate")
    payment_channel_to_fund_source_mappings: Optional[List[GetSavingsProductsPaymentChannelToFundSourceMappings]] = Field(default=None, alias="paymentChannelToFundSourceMappings")
    penalty_to_income_account_mappings: Optional[List[GetSavingsProductsPenaltyToIncomeAccountMappings]] = Field(default=None, alias="penaltyToIncomeAccountMappings")
    short_name: Optional[StrictStr] = Field(default=None, alias="shortName")
    withdrawal_fee_for_transfers: Optional[StrictBool] = Field(default=None, alias="withdrawalFeeForTransfers")
    __properties: ClassVar[List[str]] = ["accountingMappings", "accountingRule", "charges", "currency", "description", "feeToIncomeAccountMappings", "id", "interestCalculationDaysInYearType", "interestCalculationType", "interestCompoundingPeriodType", "interestPostingPeriodType", "name", "nominalAnnualInterestRate", "paymentChannelToFundSourceMappings", "penaltyToIncomeAccountMappings", "shortName", "withdrawalFeeForTransfers"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetSavingsProductsProductIdResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of accounting_mappings
        if self.accounting_mappings:
            _dict['accountingMappings'] = self.accounting_mappings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accounting_rule
        if self.accounting_rule:
            _dict['accountingRule'] = self.accounting_rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fee_to_income_account_mappings (list)
        _items = []
        if self.fee_to_income_account_mappings:
            for _item_fee_to_income_account_mappings in self.fee_to_income_account_mappings:
                if _item_fee_to_income_account_mappings:
                    _items.append(_item_fee_to_income_account_mappings.to_dict())
            _dict['feeToIncomeAccountMappings'] = _items
        # override the default output from pydantic by calling `to_dict()` of interest_calculation_days_in_year_type
        if self.interest_calculation_days_in_year_type:
            _dict['interestCalculationDaysInYearType'] = self.interest_calculation_days_in_year_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interest_calculation_type
        if self.interest_calculation_type:
            _dict['interestCalculationType'] = self.interest_calculation_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interest_compounding_period_type
        if self.interest_compounding_period_type:
            _dict['interestCompoundingPeriodType'] = self.interest_compounding_period_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interest_posting_period_type
        if self.interest_posting_period_type:
            _dict['interestPostingPeriodType'] = self.interest_posting_period_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in payment_channel_to_fund_source_mappings (list)
        _items = []
        if self.payment_channel_to_fund_source_mappings:
            for _item_payment_channel_to_fund_source_mappings in self.payment_channel_to_fund_source_mappings:
                if _item_payment_channel_to_fund_source_mappings:
                    _items.append(_item_payment_channel_to_fund_source_mappings.to_dict())
            _dict['paymentChannelToFundSourceMappings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in penalty_to_income_account_mappings (list)
        _items = []
        if self.penalty_to_income_account_mappings:
            for _item_penalty_to_income_account_mappings in self.penalty_to_income_account_mappings:
                if _item_penalty_to_income_account_mappings:
                    _items.append(_item_penalty_to_income_account_mappings.to_dict())
            _dict['penaltyToIncomeAccountMappings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetSavingsProductsProductIdResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountingMappings": GetSavingsProductsAccountingMappings.from_dict(obj["accountingMappings"]) if obj.get("accountingMappings") is not None else None,
            "accountingRule": GetSavingsProductsAccountingRule.from_dict(obj["accountingRule"]) if obj.get("accountingRule") is not None else None,
            "charges": obj.get("charges"),
            "currency": GetSavingsCurrency.from_dict(obj["currency"]) if obj.get("currency") is not None else None,
            "description": obj.get("description"),
            "feeToIncomeAccountMappings": [GetSavingsProductsFeeToIncomeAccountMappings.from_dict(_item) for _item in obj["feeToIncomeAccountMappings"]] if obj.get("feeToIncomeAccountMappings") is not None else None,
            "id": obj.get("id"),
            "interestCalculationDaysInYearType": GetSavingsProductsInterestCalculationDaysInYearType.from_dict(obj["interestCalculationDaysInYearType"]) if obj.get("interestCalculationDaysInYearType") is not None else None,
            "interestCalculationType": GetSavingsProductsInterestCalculationType.from_dict(obj["interestCalculationType"]) if obj.get("interestCalculationType") is not None else None,
            "interestCompoundingPeriodType": GetSavingsProductsInterestCompoundingPeriodType.from_dict(obj["interestCompoundingPeriodType"]) if obj.get("interestCompoundingPeriodType") is not None else None,
            "interestPostingPeriodType": GetSavingsProductsInterestPostingPeriodType.from_dict(obj["interestPostingPeriodType"]) if obj.get("interestPostingPeriodType") is not None else None,
            "name": obj.get("name"),
            "nominalAnnualInterestRate": obj.get("nominalAnnualInterestRate"),
            "paymentChannelToFundSourceMappings": [GetSavingsProductsPaymentChannelToFundSourceMappings.from_dict(_item) for _item in obj["paymentChannelToFundSourceMappings"]] if obj.get("paymentChannelToFundSourceMappings") is not None else None,
            "penaltyToIncomeAccountMappings": [GetSavingsProductsPenaltyToIncomeAccountMappings.from_dict(_item) for _item in obj["penaltyToIncomeAccountMappings"]] if obj.get("penaltyToIncomeAccountMappings") is not None else None,
            "shortName": obj.get("shortName"),
            "withdrawalFeeForTransfers": obj.get("withdrawalFeeForTransfers")
        })
        return _obj


