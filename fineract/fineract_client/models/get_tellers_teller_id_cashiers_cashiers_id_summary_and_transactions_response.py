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
from fineract_client.models.page_cashier_transaction_data import PageCashierTransactionData
from typing import Optional, Set
from typing_extensions import Self

class GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse(BaseModel):
    """
    GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse
    """ # noqa: E501
    cashier_id: Optional[StrictInt] = Field(default=None, alias="cashierId")
    cashier_name: Optional[StrictStr] = Field(default=None, alias="cashierName")
    cashier_transactions: Optional[PageCashierTransactionData] = Field(default=None, alias="cashierTransactions")
    net_cash: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="netCash")
    office_name: Optional[StrictStr] = Field(default=None, alias="officeName")
    sum_cash_allocation: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sumCashAllocation")
    sum_cash_settlement: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sumCashSettlement")
    sum_inward_cash: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sumInwardCash")
    sum_outward_cash: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sumOutwardCash")
    teller_id: Optional[StrictInt] = Field(default=None, alias="tellerId")
    teller_name: Optional[StrictStr] = Field(default=None, alias="tellerName")
    __properties: ClassVar[List[str]] = ["cashierId", "cashierName", "cashierTransactions", "netCash", "officeName", "sumCashAllocation", "sumCashSettlement", "sumInwardCash", "sumOutwardCash", "tellerId", "tellerName"]

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
        """Create an instance of GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cashier_transactions
        if self.cashier_transactions:
            _dict['cashierTransactions'] = self.cashier_transactions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetTellersTellerIdCashiersCashiersIdSummaryAndTransactionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cashierId": obj.get("cashierId"),
            "cashierName": obj.get("cashierName"),
            "cashierTransactions": PageCashierTransactionData.from_dict(obj["cashierTransactions"]) if obj.get("cashierTransactions") is not None else None,
            "netCash": obj.get("netCash"),
            "officeName": obj.get("officeName"),
            "sumCashAllocation": obj.get("sumCashAllocation"),
            "sumCashSettlement": obj.get("sumCashSettlement"),
            "sumInwardCash": obj.get("sumInwardCash"),
            "sumOutwardCash": obj.get("sumOutwardCash"),
            "tellerId": obj.get("tellerId"),
            "tellerName": obj.get("tellerName")
        })
        return _obj


