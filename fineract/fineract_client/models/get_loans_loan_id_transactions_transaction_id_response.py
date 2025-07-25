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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from fineract_client.models.get_loan_transaction_relation import GetLoanTransactionRelation
from fineract_client.models.get_loans_currency import GetLoansCurrency
from fineract_client.models.get_loans_loan_id_loan_charge_paid_by_data import GetLoansLoanIdLoanChargePaidByData
from fineract_client.models.get_loans_type import GetLoansType
from fineract_client.models.payment_detail_data import PaymentDetailData
from typing import Optional, Set
from typing_extensions import Self

class GetLoansLoanIdTransactionsTransactionIdResponse(BaseModel):
    """
    GetLoansLoanIdTransactionsTransactionIdResponse
    """ # noqa: E501
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    currency: Optional[GetLoansCurrency] = None
    var_date: Optional[date] = Field(default=None, alias="date")
    external_id: Optional[StrictStr] = Field(default=None, alias="externalId")
    fee_charges_portion: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="feeChargesPortion")
    id: Optional[StrictInt] = None
    interest_portion: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="interestPortion")
    loan_charge_paid_by_list: Optional[List[GetLoansLoanIdLoanChargePaidByData]] = Field(default=None, alias="loanChargePaidByList")
    manually_reversed: Optional[StrictBool] = Field(default=None, alias="manuallyReversed")
    net_disbursal_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="netDisbursalAmount")
    outstanding_loan_balance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="outstandingLoanBalance")
    overpayment_portion: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="overpaymentPortion")
    payment_detail_data: Optional[PaymentDetailData] = Field(default=None, alias="paymentDetailData")
    penalty_charges_portion: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="penaltyChargesPortion")
    possible_next_repayment_date: Optional[date] = Field(default=None, alias="possibleNextRepaymentDate")
    principal_portion: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="principalPortion")
    reversal_external_id: Optional[StrictStr] = Field(default=None, alias="reversalExternalId")
    reversed_on_date: Optional[date] = Field(default=None, alias="reversedOnDate")
    submitted_on_date: Optional[date] = Field(default=None, alias="submittedOnDate")
    transaction_relations: Optional[List[GetLoanTransactionRelation]] = Field(default=None, alias="transactionRelations")
    type: Optional[GetLoansType] = None
    unrecognized_income_portion: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unrecognizedIncomePortion")
    __properties: ClassVar[List[str]] = ["amount", "currency", "date", "externalId", "feeChargesPortion", "id", "interestPortion", "loanChargePaidByList", "manuallyReversed", "netDisbursalAmount", "outstandingLoanBalance", "overpaymentPortion", "paymentDetailData", "penaltyChargesPortion", "possibleNextRepaymentDate", "principalPortion", "reversalExternalId", "reversedOnDate", "submittedOnDate", "transactionRelations", "type", "unrecognizedIncomePortion"]

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
        """Create an instance of GetLoansLoanIdTransactionsTransactionIdResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in loan_charge_paid_by_list (list)
        _items = []
        if self.loan_charge_paid_by_list:
            for _item_loan_charge_paid_by_list in self.loan_charge_paid_by_list:
                if _item_loan_charge_paid_by_list:
                    _items.append(_item_loan_charge_paid_by_list.to_dict())
            _dict['loanChargePaidByList'] = _items
        # override the default output from pydantic by calling `to_dict()` of payment_detail_data
        if self.payment_detail_data:
            _dict['paymentDetailData'] = self.payment_detail_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in transaction_relations (list)
        _items = []
        if self.transaction_relations:
            for _item_transaction_relations in self.transaction_relations:
                if _item_transaction_relations:
                    _items.append(_item_transaction_relations.to_dict())
            _dict['transactionRelations'] = _items
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLoansLoanIdTransactionsTransactionIdResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "currency": GetLoansCurrency.from_dict(obj["currency"]) if obj.get("currency") is not None else None,
            "date": obj.get("date"),
            "externalId": obj.get("externalId"),
            "feeChargesPortion": obj.get("feeChargesPortion"),
            "id": obj.get("id"),
            "interestPortion": obj.get("interestPortion"),
            "loanChargePaidByList": [GetLoansLoanIdLoanChargePaidByData.from_dict(_item) for _item in obj["loanChargePaidByList"]] if obj.get("loanChargePaidByList") is not None else None,
            "manuallyReversed": obj.get("manuallyReversed"),
            "netDisbursalAmount": obj.get("netDisbursalAmount"),
            "outstandingLoanBalance": obj.get("outstandingLoanBalance"),
            "overpaymentPortion": obj.get("overpaymentPortion"),
            "paymentDetailData": PaymentDetailData.from_dict(obj["paymentDetailData"]) if obj.get("paymentDetailData") is not None else None,
            "penaltyChargesPortion": obj.get("penaltyChargesPortion"),
            "possibleNextRepaymentDate": obj.get("possibleNextRepaymentDate"),
            "principalPortion": obj.get("principalPortion"),
            "reversalExternalId": obj.get("reversalExternalId"),
            "reversedOnDate": obj.get("reversedOnDate"),
            "submittedOnDate": obj.get("submittedOnDate"),
            "transactionRelations": [GetLoanTransactionRelation.from_dict(_item) for _item in obj["transactionRelations"]] if obj.get("transactionRelations") is not None else None,
            "type": GetLoansType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "unrecognizedIncomePortion": obj.get("unrecognizedIncomePortion")
        })
        return _obj


