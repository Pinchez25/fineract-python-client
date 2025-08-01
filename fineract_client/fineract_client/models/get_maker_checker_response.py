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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetMakerCheckerResponse(BaseModel):
    """
    GetMakerCheckerResponse
    """ # noqa: E501
    action_name: Optional[StrictStr] = Field(default=None, alias="actionName")
    checked_on_date: Optional[datetime] = Field(default=None, alias="checkedOnDate")
    checker: Optional[StrictStr] = None
    client_id: Optional[StrictInt] = Field(default=None, alias="clientId")
    client_name: Optional[StrictStr] = Field(default=None, alias="clientName")
    command_as_json: Optional[StrictStr] = Field(default=None, alias="commandAsJson")
    entity_name: Optional[StrictStr] = Field(default=None, alias="entityName")
    group_level_name: Optional[StrictStr] = Field(default=None, alias="groupLevelName")
    group_name: Optional[StrictStr] = Field(default=None, alias="groupName")
    id: Optional[StrictInt] = None
    loan_account_no: Optional[StrictStr] = Field(default=None, alias="loanAccountNo")
    loan_id: Optional[StrictInt] = Field(default=None, alias="loanId")
    made_on_date: Optional[datetime] = Field(default=None, alias="madeOnDate")
    maker: Optional[StrictStr] = None
    office_name: Optional[StrictStr] = Field(default=None, alias="officeName")
    processing_result: Optional[StrictStr] = Field(default=None, alias="processingResult")
    resource_id: Optional[StrictInt] = Field(default=None, alias="resourceId")
    savings_account_no: Optional[StrictStr] = Field(default=None, alias="savingsAccountNo")
    subresource_id: Optional[StrictInt] = Field(default=None, alias="subresourceId")
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["actionName", "checkedOnDate", "checker", "clientId", "clientName", "commandAsJson", "entityName", "groupLevelName", "groupName", "id", "loanAccountNo", "loanId", "madeOnDate", "maker", "officeName", "processingResult", "resourceId", "savingsAccountNo", "subresourceId", "url"]

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
        """Create an instance of GetMakerCheckerResponse from a JSON string"""
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
        """Create an instance of GetMakerCheckerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actionName": obj.get("actionName"),
            "checkedOnDate": obj.get("checkedOnDate"),
            "checker": obj.get("checker"),
            "clientId": obj.get("clientId"),
            "clientName": obj.get("clientName"),
            "commandAsJson": obj.get("commandAsJson"),
            "entityName": obj.get("entityName"),
            "groupLevelName": obj.get("groupLevelName"),
            "groupName": obj.get("groupName"),
            "id": obj.get("id"),
            "loanAccountNo": obj.get("loanAccountNo"),
            "loanId": obj.get("loanId"),
            "madeOnDate": obj.get("madeOnDate"),
            "maker": obj.get("maker"),
            "officeName": obj.get("officeName"),
            "processingResult": obj.get("processingResult"),
            "resourceId": obj.get("resourceId"),
            "savingsAccountNo": obj.get("savingsAccountNo"),
            "subresourceId": obj.get("subresourceId"),
            "url": obj.get("url")
        })
        return _obj


