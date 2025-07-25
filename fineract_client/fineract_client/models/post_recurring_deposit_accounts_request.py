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
from typing import Optional, Set
from typing_extensions import Self

class PostRecurringDepositAccountsRequest(BaseModel):
    """
    PostRecurringDepositAccountsRequest
    """ # noqa: E501
    client_id: Optional[StrictInt] = Field(default=None, alias="clientId")
    date_format: Optional[StrictStr] = Field(default=None, alias="dateFormat")
    deposit_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="depositAmount")
    deposit_period: Optional[StrictInt] = Field(default=None, alias="depositPeriod")
    deposit_period_frequency_id: Optional[StrictInt] = Field(default=None, alias="depositPeriodFrequencyId")
    is_calendar_inherited: Optional[StrictBool] = Field(default=None, alias="isCalendarInherited")
    locale: Optional[StrictStr] = None
    mandatory_recommended_deposit_amount: Optional[StrictInt] = Field(default=None, alias="mandatoryRecommendedDepositAmount")
    product_id: Optional[StrictInt] = Field(default=None, alias="productId")
    recurring_frequency: Optional[StrictInt] = Field(default=None, alias="recurringFrequency")
    recurring_frequency_type: Optional[StrictInt] = Field(default=None, alias="recurringFrequencyType")
    submitted_on_date: Optional[StrictStr] = Field(default=None, alias="submittedOnDate")
    __properties: ClassVar[List[str]] = ["clientId", "dateFormat", "depositAmount", "depositPeriod", "depositPeriodFrequencyId", "isCalendarInherited", "locale", "mandatoryRecommendedDepositAmount", "productId", "recurringFrequency", "recurringFrequencyType", "submittedOnDate"]

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
        """Create an instance of PostRecurringDepositAccountsRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostRecurringDepositAccountsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientId": obj.get("clientId"),
            "dateFormat": obj.get("dateFormat"),
            "depositAmount": obj.get("depositAmount"),
            "depositPeriod": obj.get("depositPeriod"),
            "depositPeriodFrequencyId": obj.get("depositPeriodFrequencyId"),
            "isCalendarInherited": obj.get("isCalendarInherited"),
            "locale": obj.get("locale"),
            "mandatoryRecommendedDepositAmount": obj.get("mandatoryRecommendedDepositAmount"),
            "productId": obj.get("productId"),
            "recurringFrequency": obj.get("recurringFrequency"),
            "recurringFrequencyType": obj.get("recurringFrequencyType"),
            "submittedOnDate": obj.get("submittedOnDate")
        })
        return _obj


