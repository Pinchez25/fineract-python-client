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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from fineract_client.models.get_from_account_standing_instruction_swagger import GetFromAccountStandingInstructionSwagger
from fineract_client.models.get_from_account_type_standing_instruction_swagger import GetFromAccountTypeStandingInstructionSwagger
from fineract_client.models.get_from_client_standing_instruction_swagger import GetFromClientStandingInstructionSwagger
from fineract_client.models.get_from_office_standing_instruction_swagger import GetFromOfficeStandingInstructionSwagger
from fineract_client.models.get_instruction_type_standing_instruction_swagger import GetInstructionTypeStandingInstructionSwagger
from fineract_client.models.get_priority_standing_instruction_swagger import GetPriorityStandingInstructionSwagger
from fineract_client.models.get_recurrence_frequency_standing_instruction_swagger import GetRecurrenceFrequencyStandingInstructionSwagger
from fineract_client.models.get_recurrence_type_standing_instruction_swagger import GetRecurrenceTypeStandingInstructionSwagger
from fineract_client.models.get_status_standing_instruction_swagger import GetStatusStandingInstructionSwagger
from fineract_client.models.get_to_account_standing_instruction_swagger import GetToAccountStandingInstructionSwagger
from fineract_client.models.get_to_account_type_standing_instruction_swagger import GetToAccountTypeStandingInstructionSwagger
from fineract_client.models.get_to_client_standing_instruction_swagger import GetToClientStandingInstructionSwagger
from fineract_client.models.get_to_office_standing_instruction_swagger import GetToOfficeStandingInstructionSwagger
from fineract_client.models.get_transfer_type_standing_instruction_swagger import GetTransferTypeStandingInstructionSwagger
from typing import Optional, Set
from typing_extensions import Self

class GetPageItemsStandingInstructionSwagger(BaseModel):
    """
    GetPageItemsStandingInstructionSwagger
    """ # noqa: E501
    account_detail_id: Optional[StrictInt] = Field(default=None, alias="accountDetailId")
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    from_account: Optional[GetFromAccountStandingInstructionSwagger] = Field(default=None, alias="fromAccount")
    from_account_type: Optional[GetFromAccountTypeStandingInstructionSwagger] = Field(default=None, alias="fromAccountType")
    from_client: Optional[GetFromClientStandingInstructionSwagger] = Field(default=None, alias="fromClient")
    from_office: Optional[GetFromOfficeStandingInstructionSwagger] = Field(default=None, alias="fromOffice")
    id: Optional[StrictInt] = None
    instruction_type: Optional[GetInstructionTypeStandingInstructionSwagger] = Field(default=None, alias="instructionType")
    name: Optional[StrictStr] = None
    priority: Optional[GetPriorityStandingInstructionSwagger] = None
    recurrence_frequency: Optional[GetRecurrenceFrequencyStandingInstructionSwagger] = Field(default=None, alias="recurrenceFrequency")
    recurrence_interval: Optional[StrictInt] = Field(default=None, alias="recurrenceInterval")
    recurrence_on_month_day: Optional[date] = Field(default=None, alias="recurrenceOnMonthDay")
    recurrence_type: Optional[GetRecurrenceTypeStandingInstructionSwagger] = Field(default=None, alias="recurrenceType")
    status: Optional[GetStatusStandingInstructionSwagger] = None
    to_account: Optional[GetToAccountStandingInstructionSwagger] = Field(default=None, alias="toAccount")
    to_account_type: Optional[GetToAccountTypeStandingInstructionSwagger] = Field(default=None, alias="toAccountType")
    to_client: Optional[GetToClientStandingInstructionSwagger] = Field(default=None, alias="toClient")
    to_office: Optional[GetToOfficeStandingInstructionSwagger] = Field(default=None, alias="toOffice")
    transfer_type: Optional[GetTransferTypeStandingInstructionSwagger] = Field(default=None, alias="transferType")
    valid_from: Optional[date] = Field(default=None, alias="validFrom")
    __properties: ClassVar[List[str]] = ["accountDetailId", "amount", "fromAccount", "fromAccountType", "fromClient", "fromOffice", "id", "instructionType", "name", "priority", "recurrenceFrequency", "recurrenceInterval", "recurrenceOnMonthDay", "recurrenceType", "status", "toAccount", "toAccountType", "toClient", "toOffice", "transferType", "validFrom"]

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
        """Create an instance of GetPageItemsStandingInstructionSwagger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of from_account
        if self.from_account:
            _dict['fromAccount'] = self.from_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of from_account_type
        if self.from_account_type:
            _dict['fromAccountType'] = self.from_account_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of from_client
        if self.from_client:
            _dict['fromClient'] = self.from_client.to_dict()
        # override the default output from pydantic by calling `to_dict()` of from_office
        if self.from_office:
            _dict['fromOffice'] = self.from_office.to_dict()
        # override the default output from pydantic by calling `to_dict()` of instruction_type
        if self.instruction_type:
            _dict['instructionType'] = self.instruction_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recurrence_frequency
        if self.recurrence_frequency:
            _dict['recurrenceFrequency'] = self.recurrence_frequency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recurrence_type
        if self.recurrence_type:
            _dict['recurrenceType'] = self.recurrence_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_account
        if self.to_account:
            _dict['toAccount'] = self.to_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_account_type
        if self.to_account_type:
            _dict['toAccountType'] = self.to_account_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_client
        if self.to_client:
            _dict['toClient'] = self.to_client.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_office
        if self.to_office:
            _dict['toOffice'] = self.to_office.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transfer_type
        if self.transfer_type:
            _dict['transferType'] = self.transfer_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetPageItemsStandingInstructionSwagger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountDetailId": obj.get("accountDetailId"),
            "amount": obj.get("amount"),
            "fromAccount": GetFromAccountStandingInstructionSwagger.from_dict(obj["fromAccount"]) if obj.get("fromAccount") is not None else None,
            "fromAccountType": GetFromAccountTypeStandingInstructionSwagger.from_dict(obj["fromAccountType"]) if obj.get("fromAccountType") is not None else None,
            "fromClient": GetFromClientStandingInstructionSwagger.from_dict(obj["fromClient"]) if obj.get("fromClient") is not None else None,
            "fromOffice": GetFromOfficeStandingInstructionSwagger.from_dict(obj["fromOffice"]) if obj.get("fromOffice") is not None else None,
            "id": obj.get("id"),
            "instructionType": GetInstructionTypeStandingInstructionSwagger.from_dict(obj["instructionType"]) if obj.get("instructionType") is not None else None,
            "name": obj.get("name"),
            "priority": GetPriorityStandingInstructionSwagger.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "recurrenceFrequency": GetRecurrenceFrequencyStandingInstructionSwagger.from_dict(obj["recurrenceFrequency"]) if obj.get("recurrenceFrequency") is not None else None,
            "recurrenceInterval": obj.get("recurrenceInterval"),
            "recurrenceOnMonthDay": obj.get("recurrenceOnMonthDay"),
            "recurrenceType": GetRecurrenceTypeStandingInstructionSwagger.from_dict(obj["recurrenceType"]) if obj.get("recurrenceType") is not None else None,
            "status": GetStatusStandingInstructionSwagger.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "toAccount": GetToAccountStandingInstructionSwagger.from_dict(obj["toAccount"]) if obj.get("toAccount") is not None else None,
            "toAccountType": GetToAccountTypeStandingInstructionSwagger.from_dict(obj["toAccountType"]) if obj.get("toAccountType") is not None else None,
            "toClient": GetToClientStandingInstructionSwagger.from_dict(obj["toClient"]) if obj.get("toClient") is not None else None,
            "toOffice": GetToOfficeStandingInstructionSwagger.from_dict(obj["toOffice"]) if obj.get("toOffice") is not None else None,
            "transferType": GetTransferTypeStandingInstructionSwagger.from_dict(obj["transferType"]) if obj.get("transferType") is not None else None,
            "validFrom": obj.get("validFrom")
        })
        return _obj


