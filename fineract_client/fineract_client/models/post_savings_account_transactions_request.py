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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class PostSavingsAccountTransactionsRequest(BaseModel):
    """
    PostSavingsAccountTransactionsRequest
    """ # noqa: E501
    date_format: Optional[StrictStr] = Field(default=None, alias="dateFormat")
    lien_allowed: Optional[StrictStr] = Field(default=None, alias="lienAllowed")
    locale: Optional[StrictStr] = None
    payment_type_id: Optional[StrictInt] = Field(default=None, alias="paymentTypeId")
    reason_for_block: Optional[StrictStr] = Field(default=None, alias="reasonForBlock")
    transaction_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="transactionAmount")
    transaction_date: Optional[StrictStr] = Field(default=None, alias="transactionDate")
    __properties: ClassVar[List[str]] = ["dateFormat", "lienAllowed", "locale", "paymentTypeId", "reasonForBlock", "transactionAmount", "transactionDate"]

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
        """Create an instance of PostSavingsAccountTransactionsRequest from a JSON string"""
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
        """Create an instance of PostSavingsAccountTransactionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dateFormat": obj.get("dateFormat"),
            "lienAllowed": obj.get("lienAllowed"),
            "locale": obj.get("locale"),
            "paymentTypeId": obj.get("paymentTypeId"),
            "reasonForBlock": obj.get("reasonForBlock"),
            "transactionAmount": obj.get("transactionAmount"),
            "transactionDate": obj.get("transactionDate")
        })
        return _obj


