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
from fineract_client.models.get_recurring_deposit_products_accounting_rule import GetRecurringDepositProductsAccountingRule
from fineract_client.models.get_recurring_deposit_products_currency import GetRecurringDepositProductsCurrency
from fineract_client.models.get_recurring_deposit_products_interest_calculation_days_in_year_type import GetRecurringDepositProductsInterestCalculationDaysInYearType
from fineract_client.models.get_recurring_deposit_products_interest_calculation_type import GetRecurringDepositProductsInterestCalculationType
from fineract_client.models.get_recurring_deposit_products_interest_compounding_period_type import GetRecurringDepositProductsInterestCompoundingPeriodType
from fineract_client.models.get_recurring_deposit_products_interest_posting_period_type import GetRecurringDepositProductsInterestPostingPeriodType
from fineract_client.models.get_recurring_deposit_products_max_deposit_term_type import GetRecurringDepositProductsMaxDepositTermType
from fineract_client.models.get_recurring_deposit_products_min_deposit_term_type import GetRecurringDepositProductsMinDepositTermType
from fineract_client.models.get_recurring_deposit_products_recurring_deposit_frequency_type import GetRecurringDepositProductsRecurringDepositFrequencyType
from typing import Optional, Set
from typing_extensions import Self

class GetRecurringDepositProductsResponse(BaseModel):
    """
    GetRecurringDepositProductsResponse
    """ # noqa: E501
    accounting_rule: Optional[GetRecurringDepositProductsAccountingRule] = Field(default=None, alias="accountingRule")
    currency: Optional[GetRecurringDepositProductsCurrency] = None
    description: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    interest_calculation_days_in_year_type: Optional[GetRecurringDepositProductsInterestCalculationDaysInYearType] = Field(default=None, alias="interestCalculationDaysInYearType")
    interest_calculation_type: Optional[GetRecurringDepositProductsInterestCalculationType] = Field(default=None, alias="interestCalculationType")
    interest_compounding_period_type: Optional[GetRecurringDepositProductsInterestCompoundingPeriodType] = Field(default=None, alias="interestCompoundingPeriodType")
    interest_posting_period_type: Optional[GetRecurringDepositProductsInterestPostingPeriodType] = Field(default=None, alias="interestPostingPeriodType")
    max_deposit_term: Optional[StrictInt] = Field(default=None, alias="maxDepositTerm")
    max_deposit_term_type: Optional[GetRecurringDepositProductsMaxDepositTermType] = Field(default=None, alias="maxDepositTermType")
    min_deposit_term: Optional[StrictInt] = Field(default=None, alias="minDepositTerm")
    min_deposit_term_type: Optional[GetRecurringDepositProductsMinDepositTermType] = Field(default=None, alias="minDepositTermType")
    name: Optional[StrictStr] = None
    nominal_annual_interest_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="nominalAnnualInterestRate")
    pre_closure_penal_applicable: Optional[StrictBool] = Field(default=None, alias="preClosurePenalApplicable")
    recurring_deposit_frequency: Optional[StrictInt] = Field(default=None, alias="recurringDepositFrequency")
    recurring_deposit_frequency_type: Optional[GetRecurringDepositProductsRecurringDepositFrequencyType] = Field(default=None, alias="recurringDepositFrequencyType")
    short_name: Optional[StrictStr] = Field(default=None, alias="shortName")
    __properties: ClassVar[List[str]] = ["accountingRule", "currency", "description", "id", "interestCalculationDaysInYearType", "interestCalculationType", "interestCompoundingPeriodType", "interestPostingPeriodType", "maxDepositTerm", "maxDepositTermType", "minDepositTerm", "minDepositTermType", "name", "nominalAnnualInterestRate", "preClosurePenalApplicable", "recurringDepositFrequency", "recurringDepositFrequencyType", "shortName"]

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
        """Create an instance of GetRecurringDepositProductsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of accounting_rule
        if self.accounting_rule:
            _dict['accountingRule'] = self.accounting_rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of max_deposit_term_type
        if self.max_deposit_term_type:
            _dict['maxDepositTermType'] = self.max_deposit_term_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of min_deposit_term_type
        if self.min_deposit_term_type:
            _dict['minDepositTermType'] = self.min_deposit_term_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recurring_deposit_frequency_type
        if self.recurring_deposit_frequency_type:
            _dict['recurringDepositFrequencyType'] = self.recurring_deposit_frequency_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetRecurringDepositProductsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountingRule": GetRecurringDepositProductsAccountingRule.from_dict(obj["accountingRule"]) if obj.get("accountingRule") is not None else None,
            "currency": GetRecurringDepositProductsCurrency.from_dict(obj["currency"]) if obj.get("currency") is not None else None,
            "description": obj.get("description"),
            "id": obj.get("id"),
            "interestCalculationDaysInYearType": GetRecurringDepositProductsInterestCalculationDaysInYearType.from_dict(obj["interestCalculationDaysInYearType"]) if obj.get("interestCalculationDaysInYearType") is not None else None,
            "interestCalculationType": GetRecurringDepositProductsInterestCalculationType.from_dict(obj["interestCalculationType"]) if obj.get("interestCalculationType") is not None else None,
            "interestCompoundingPeriodType": GetRecurringDepositProductsInterestCompoundingPeriodType.from_dict(obj["interestCompoundingPeriodType"]) if obj.get("interestCompoundingPeriodType") is not None else None,
            "interestPostingPeriodType": GetRecurringDepositProductsInterestPostingPeriodType.from_dict(obj["interestPostingPeriodType"]) if obj.get("interestPostingPeriodType") is not None else None,
            "maxDepositTerm": obj.get("maxDepositTerm"),
            "maxDepositTermType": GetRecurringDepositProductsMaxDepositTermType.from_dict(obj["maxDepositTermType"]) if obj.get("maxDepositTermType") is not None else None,
            "minDepositTerm": obj.get("minDepositTerm"),
            "minDepositTermType": GetRecurringDepositProductsMinDepositTermType.from_dict(obj["minDepositTermType"]) if obj.get("minDepositTermType") is not None else None,
            "name": obj.get("name"),
            "nominalAnnualInterestRate": obj.get("nominalAnnualInterestRate"),
            "preClosurePenalApplicable": obj.get("preClosurePenalApplicable"),
            "recurringDepositFrequency": obj.get("recurringDepositFrequency"),
            "recurringDepositFrequencyType": GetRecurringDepositProductsRecurringDepositFrequencyType.from_dict(obj["recurringDepositFrequencyType"]) if obj.get("recurringDepositFrequencyType") is not None else None,
            "shortName": obj.get("shortName")
        })
        return _obj


