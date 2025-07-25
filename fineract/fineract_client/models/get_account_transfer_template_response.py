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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from fineract_client.models.get_account_options import GetAccountOptions
from fineract_client.models.get_from_account_options import GetFromAccountOptions
from typing import Optional, Set
from typing_extensions import Self

class GetAccountTransferTemplateResponse(BaseModel):
    """
    GetAccountTransferTemplateResponse
    """ # noqa: E501
    account_type_options: Optional[List[GetAccountOptions]] = Field(default=None, alias="accountTypeOptions")
    from_account_type_options: Optional[List[GetFromAccountOptions]] = Field(default=None, alias="fromAccountTypeOptions")
    to_account_type_options: Optional[List[GetFromAccountOptions]] = Field(default=None, alias="toAccountTypeOptions")
    __properties: ClassVar[List[str]] = ["accountTypeOptions", "fromAccountTypeOptions", "toAccountTypeOptions"]

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
        """Create an instance of GetAccountTransferTemplateResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in account_type_options (list)
        _items = []
        if self.account_type_options:
            for _item_account_type_options in self.account_type_options:
                if _item_account_type_options:
                    _items.append(_item_account_type_options.to_dict())
            _dict['accountTypeOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in from_account_type_options (list)
        _items = []
        if self.from_account_type_options:
            for _item_from_account_type_options in self.from_account_type_options:
                if _item_from_account_type_options:
                    _items.append(_item_from_account_type_options.to_dict())
            _dict['fromAccountTypeOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in to_account_type_options (list)
        _items = []
        if self.to_account_type_options:
            for _item_to_account_type_options in self.to_account_type_options:
                if _item_to_account_type_options:
                    _items.append(_item_to_account_type_options.to_dict())
            _dict['toAccountTypeOptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetAccountTransferTemplateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountTypeOptions": [GetAccountOptions.from_dict(_item) for _item in obj["accountTypeOptions"]] if obj.get("accountTypeOptions") is not None else None,
            "fromAccountTypeOptions": [GetFromAccountOptions.from_dict(_item) for _item in obj["fromAccountTypeOptions"]] if obj.get("fromAccountTypeOptions") is not None else None,
            "toAccountTypeOptions": [GetFromAccountOptions.from_dict(_item) for _item in obj["toAccountTypeOptions"]] if obj.get("toAccountTypeOptions") is not None else None
        })
        return _obj


