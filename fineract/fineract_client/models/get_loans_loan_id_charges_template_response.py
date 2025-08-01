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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from fineract_client.models.get_loan_charge_template_charge_options import GetLoanChargeTemplateChargeOptions
from typing import Optional, Set
from typing_extensions import Self

class GetLoansLoanIdChargesTemplateResponse(BaseModel):
    """
    GetLoansLoanIdChargesTemplateResponse
    """ # noqa: E501
    amount_paid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="amountPaid")
    amount_waived: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="amountWaived")
    amount_written_off: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="amountWrittenOff")
    charge_options: Optional[List[GetLoanChargeTemplateChargeOptions]] = Field(default=None, alias="chargeOptions")
    penalty: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["amountPaid", "amountWaived", "amountWrittenOff", "chargeOptions", "penalty"]

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
        """Create an instance of GetLoansLoanIdChargesTemplateResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in charge_options (list)
        _items = []
        if self.charge_options:
            for _item_charge_options in self.charge_options:
                if _item_charge_options:
                    _items.append(_item_charge_options.to_dict())
            _dict['chargeOptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLoansLoanIdChargesTemplateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amountPaid": obj.get("amountPaid"),
            "amountWaived": obj.get("amountWaived"),
            "amountWrittenOff": obj.get("amountWrittenOff"),
            "chargeOptions": [GetLoanChargeTemplateChargeOptions.from_dict(_item) for _item in obj["chargeOptions"]] if obj.get("chargeOptions") is not None else None,
            "penalty": obj.get("penalty")
        })
        return _obj


