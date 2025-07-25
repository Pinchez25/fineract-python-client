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
from fineract_client.models.office_data import OfficeData
from fineract_client.models.role_data import RoleData
from typing import Optional, Set
from typing_extensions import Self

class GetUsersTemplateResponse(BaseModel):
    """
    GetUsersTemplateResponse
    """ # noqa: E501
    allowed_offices: Optional[List[OfficeData]] = Field(default=None, alias="allowedOffices")
    available_roles: Optional[List[RoleData]] = Field(default=None, alias="availableRoles")
    self_service_roles: Optional[List[RoleData]] = Field(default=None, alias="selfServiceRoles")
    __properties: ClassVar[List[str]] = ["allowedOffices", "availableRoles", "selfServiceRoles"]

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
        """Create an instance of GetUsersTemplateResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in allowed_offices (list)
        _items = []
        if self.allowed_offices:
            for _item_allowed_offices in self.allowed_offices:
                if _item_allowed_offices:
                    _items.append(_item_allowed_offices.to_dict())
            _dict['allowedOffices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in available_roles (list)
        _items = []
        if self.available_roles:
            for _item_available_roles in self.available_roles:
                if _item_available_roles:
                    _items.append(_item_available_roles.to_dict())
            _dict['availableRoles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in self_service_roles (list)
        _items = []
        if self.self_service_roles:
            for _item_self_service_roles in self.self_service_roles:
                if _item_self_service_roles:
                    _items.append(_item_self_service_roles.to_dict())
            _dict['selfServiceRoles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetUsersTemplateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowedOffices": [OfficeData.from_dict(_item) for _item in obj["allowedOffices"]] if obj.get("allowedOffices") is not None else None,
            "availableRoles": [RoleData.from_dict(_item) for _item in obj["availableRoles"]] if obj.get("availableRoles") is not None else None,
            "selfServiceRoles": [RoleData.from_dict(_item) for _item in obj["selfServiceRoles"]] if obj.get("selfServiceRoles") is not None else None
        })
        return _obj


