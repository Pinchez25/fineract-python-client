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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fineract_client.models.put_data_tables_request_add_columns import PutDataTablesRequestAddColumns
from fineract_client.models.put_data_tables_request_change_columns import PutDataTablesRequestChangeColumns
from fineract_client.models.put_data_tables_request_drop_columns import PutDataTablesRequestDropColumns
from typing import Optional, Set
from typing_extensions import Self

class PutDataTablesRequest(BaseModel):
    """
    PutDataTablesRequest
    """ # noqa: E501
    add_columns: Optional[List[PutDataTablesRequestAddColumns]] = Field(default=None, alias="addColumns")
    apptable_name: Optional[StrictStr] = Field(default=None, alias="apptableName")
    change_columns: Optional[List[PutDataTablesRequestChangeColumns]] = Field(default=None, alias="changeColumns")
    drop_columns: Optional[List[PutDataTablesRequestDropColumns]] = Field(default=None, alias="dropColumns")
    __properties: ClassVar[List[str]] = ["addColumns", "apptableName", "changeColumns", "dropColumns"]

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
        """Create an instance of PutDataTablesRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in add_columns (list)
        _items = []
        if self.add_columns:
            for _item_add_columns in self.add_columns:
                if _item_add_columns:
                    _items.append(_item_add_columns.to_dict())
            _dict['addColumns'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in change_columns (list)
        _items = []
        if self.change_columns:
            for _item_change_columns in self.change_columns:
                if _item_change_columns:
                    _items.append(_item_change_columns.to_dict())
            _dict['changeColumns'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in drop_columns (list)
        _items = []
        if self.drop_columns:
            for _item_drop_columns in self.drop_columns:
                if _item_drop_columns:
                    _items.append(_item_drop_columns.to_dict())
            _dict['dropColumns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PutDataTablesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addColumns": [PutDataTablesRequestAddColumns.from_dict(_item) for _item in obj["addColumns"]] if obj.get("addColumns") is not None else None,
            "apptableName": obj.get("apptableName"),
            "changeColumns": [PutDataTablesRequestChangeColumns.from_dict(_item) for _item in obj["changeColumns"]] if obj.get("changeColumns") is not None else None,
            "dropColumns": [PutDataTablesRequestDropColumns.from_dict(_item) for _item in obj["dropColumns"]] if obj.get("dropColumns") is not None else None
        })
        return _obj


