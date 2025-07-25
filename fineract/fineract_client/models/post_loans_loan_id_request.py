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
from fineract_client.models.post_loans_loan_id_disbursement_data import PostLoansLoanIdDisbursementData
from typing import Optional, Set
from typing_extensions import Self

class PostLoansLoanIdRequest(BaseModel):
    """
    PostLoansLoanIdRequest
    """ # noqa: E501
    actual_disbursement_date: Optional[StrictStr] = Field(default=None, alias="actualDisbursementDate")
    approved_loan_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="approvedLoanAmount")
    approved_on_date: Optional[StrictStr] = Field(default=None, alias="approvedOnDate")
    assignment_date: Optional[StrictStr] = Field(default=None, alias="assignmentDate")
    date_format: Optional[StrictStr] = Field(default=None, alias="dateFormat")
    disbursement_data: Optional[List[PostLoansLoanIdDisbursementData]] = Field(default=None, description="List of PostLoansLoanIdDisbursementData", alias="disbursementData")
    expected_disbursement_date: Optional[StrictStr] = Field(default=None, alias="expectedDisbursementDate")
    external_id: Optional[StrictStr] = Field(default=None, alias="externalId")
    from_loan_officer_id: Optional[StrictInt] = Field(default=None, alias="fromLoanOfficerId")
    locale: Optional[StrictStr] = None
    note: Optional[StrictStr] = None
    payment_type_id: Optional[StrictInt] = Field(default=None, alias="paymentTypeId")
    rejected_on_date: Optional[StrictStr] = Field(default=None, alias="rejectedOnDate")
    to_loan_officer_id: Optional[StrictInt] = Field(default=None, alias="toLoanOfficerId")
    transaction_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="transactionAmount")
    unassigned_date: Optional[StrictStr] = Field(default=None, alias="unassignedDate")
    withdrawn_on_date: Optional[StrictStr] = Field(default=None, alias="withdrawnOnDate")
    __properties: ClassVar[List[str]] = ["actualDisbursementDate", "approvedLoanAmount", "approvedOnDate", "assignmentDate", "dateFormat", "disbursementData", "expectedDisbursementDate", "externalId", "fromLoanOfficerId", "locale", "note", "paymentTypeId", "rejectedOnDate", "toLoanOfficerId", "transactionAmount", "unassignedDate", "withdrawnOnDate"]

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
        """Create an instance of PostLoansLoanIdRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in disbursement_data (list)
        _items = []
        if self.disbursement_data:
            for _item_disbursement_data in self.disbursement_data:
                if _item_disbursement_data:
                    _items.append(_item_disbursement_data.to_dict())
            _dict['disbursementData'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostLoansLoanIdRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actualDisbursementDate": obj.get("actualDisbursementDate"),
            "approvedLoanAmount": obj.get("approvedLoanAmount"),
            "approvedOnDate": obj.get("approvedOnDate"),
            "assignmentDate": obj.get("assignmentDate"),
            "dateFormat": obj.get("dateFormat"),
            "disbursementData": [PostLoansLoanIdDisbursementData.from_dict(_item) for _item in obj["disbursementData"]] if obj.get("disbursementData") is not None else None,
            "expectedDisbursementDate": obj.get("expectedDisbursementDate"),
            "externalId": obj.get("externalId"),
            "fromLoanOfficerId": obj.get("fromLoanOfficerId"),
            "locale": obj.get("locale"),
            "note": obj.get("note"),
            "paymentTypeId": obj.get("paymentTypeId"),
            "rejectedOnDate": obj.get("rejectedOnDate"),
            "toLoanOfficerId": obj.get("toLoanOfficerId"),
            "transactionAmount": obj.get("transactionAmount"),
            "unassignedDate": obj.get("unassignedDate"),
            "withdrawnOnDate": obj.get("withdrawnOnDate")
        })
        return _obj


