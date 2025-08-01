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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fineract_client.models.client_identifier import ClientIdentifier
from fineract_client.models.code_value import CodeValue
from fineract_client.models.external_id import ExternalId
from fineract_client.models.image import Image
from fineract_client.models.office import Office
from fineract_client.models.staff import Staff
from typing import Optional, Set
from typing_extensions import Self

class Client(BaseModel):
    """
    Client
    """ # noqa: E501
    account_number: Optional[StrictStr] = Field(default=None, alias="accountNumber")
    account_number_requires_auto_generation: Optional[StrictBool] = Field(default=None, alias="accountNumberRequiresAutoGeneration")
    activated_by: Optional[AppUser] = Field(default=None, alias="activatedBy")
    activation_date: Optional[date] = Field(default=None, alias="activationDate")
    active: Optional[StrictBool] = None
    client_classification: Optional[CodeValue] = Field(default=None, alias="clientClassification")
    client_type: Optional[CodeValue] = Field(default=None, alias="clientType")
    closed: Optional[StrictBool] = None
    closed_by: Optional[AppUser] = Field(default=None, alias="closedBy")
    closure_date: Optional[date] = Field(default=None, alias="closureDate")
    closure_reason: Optional[CodeValue] = Field(default=None, alias="closureReason")
    created_by: StrictInt = Field(alias="createdBy")
    created_date: datetime = Field(alias="createdDate")
    created_date_time: datetime = Field(alias="createdDateTime")
    date_of_birth: Optional[date] = Field(default=None, alias="dateOfBirth")
    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    email_address: Optional[StrictStr] = Field(default=None, alias="emailAddress")
    external_id: Optional[ExternalId] = Field(default=None, alias="externalId")
    firstname: Optional[StrictStr] = None
    fullname: Optional[StrictStr] = None
    gender: Optional[CodeValue] = None
    groups: Optional[List[Group]] = None
    id: Optional[StrictInt] = None
    identifiers: Optional[List[ClientIdentifier]] = None
    image: Optional[Image] = None
    last_modified_by: StrictInt = Field(alias="lastModifiedBy")
    last_modified_date: datetime = Field(alias="lastModifiedDate")
    last_modified_date_time: datetime = Field(alias="lastModifiedDateTime")
    lastname: Optional[StrictStr] = None
    legal_form: Optional[StrictInt] = Field(default=None, alias="legalForm")
    middlename: Optional[StrictStr] = None
    mobile_no: Optional[StrictStr] = Field(default=None, alias="mobileNo")
    new: Optional[StrictBool] = None
    not_active: Optional[StrictBool] = Field(default=None, alias="notActive")
    not_pending: Optional[StrictBool] = Field(default=None, alias="notPending")
    not_staff: Optional[StrictBool] = Field(default=None, alias="notStaff")
    office: Optional[Office] = None
    office_joining_date: Optional[date] = Field(default=None, alias="officeJoiningDate")
    pending: Optional[StrictBool] = None
    proposed_transfer_date: Optional[date] = Field(default=None, alias="proposedTransferDate")
    reactivate_date: Optional[date] = Field(default=None, alias="reactivateDate")
    reactivated_by: Optional[AppUser] = Field(default=None, alias="reactivatedBy")
    rejected: Optional[StrictBool] = None
    rejected_by: Optional[AppUser] = Field(default=None, alias="rejectedBy")
    rejected_date: Optional[date] = Field(default=None, alias="rejectedDate")
    rejection_date: Optional[date] = Field(default=None, alias="rejectionDate")
    rejection_reason: Optional[CodeValue] = Field(default=None, alias="rejectionReason")
    reopened_by: Optional[AppUser] = Field(default=None, alias="reopenedBy")
    reopened_date: Optional[date] = Field(default=None, alias="reopenedDate")
    savings_account_id: Optional[StrictInt] = Field(default=None, alias="savingsAccountId")
    savings_product_id: Optional[StrictInt] = Field(default=None, alias="savingsProductId")
    staff: Optional[Staff] = None
    status: Optional[StrictInt] = None
    sub_status: Optional[CodeValue] = Field(default=None, alias="subStatus")
    submitted_on_date: Optional[date] = Field(default=None, alias="submittedOnDate")
    transfer_in_progress: Optional[StrictBool] = Field(default=None, alias="transferInProgress")
    transfer_in_progress_or_on_hold: Optional[StrictBool] = Field(default=None, alias="transferInProgressOrOnHold")
    transfer_on_hold: Optional[StrictBool] = Field(default=None, alias="transferOnHold")
    transfer_to_office: Optional[Office] = Field(default=None, alias="transferToOffice")
    withdrawal_date: Optional[date] = Field(default=None, alias="withdrawalDate")
    withdrawal_reason: Optional[CodeValue] = Field(default=None, alias="withdrawalReason")
    withdrawn: Optional[StrictBool] = None
    withdrawn_by: Optional[AppUser] = Field(default=None, alias="withdrawnBy")
    __properties: ClassVar[List[str]] = ["accountNumber", "accountNumberRequiresAutoGeneration", "activatedBy", "activationDate", "active", "clientClassification", "clientType", "closed", "closedBy", "closureDate", "closureReason", "createdBy", "createdDate", "createdDateTime", "dateOfBirth", "displayName", "emailAddress", "externalId", "firstname", "fullname", "gender", "groups", "id", "identifiers", "image", "lastModifiedBy", "lastModifiedDate", "lastModifiedDateTime", "lastname", "legalForm", "middlename", "mobileNo", "new", "notActive", "notPending", "notStaff", "office", "officeJoiningDate", "pending", "proposedTransferDate", "reactivateDate", "reactivatedBy", "rejected", "rejectedBy", "rejectedDate", "rejectionDate", "rejectionReason", "reopenedBy", "reopenedDate", "savingsAccountId", "savingsProductId", "staff", "status", "subStatus", "submittedOnDate", "transferInProgress", "transferInProgressOrOnHold", "transferOnHold", "transferToOffice", "withdrawalDate", "withdrawalReason", "withdrawn", "withdrawnBy"]

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
        """Create an instance of Client from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of activated_by
        if self.activated_by:
            _dict['activatedBy'] = self.activated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_classification
        if self.client_classification:
            _dict['clientClassification'] = self.client_classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_type
        if self.client_type:
            _dict['clientType'] = self.client_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of closed_by
        if self.closed_by:
            _dict['closedBy'] = self.closed_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of closure_reason
        if self.closure_reason:
            _dict['closureReason'] = self.closure_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_id
        if self.external_id:
            _dict['externalId'] = self.external_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gender
        if self.gender:
            _dict['gender'] = self.gender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in identifiers (list)
        _items = []
        if self.identifiers:
            for _item_identifiers in self.identifiers:
                if _item_identifiers:
                    _items.append(_item_identifiers.to_dict())
            _dict['identifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of office
        if self.office:
            _dict['office'] = self.office.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reactivated_by
        if self.reactivated_by:
            _dict['reactivatedBy'] = self.reactivated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rejected_by
        if self.rejected_by:
            _dict['rejectedBy'] = self.rejected_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rejection_reason
        if self.rejection_reason:
            _dict['rejectionReason'] = self.rejection_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reopened_by
        if self.reopened_by:
            _dict['reopenedBy'] = self.reopened_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of staff
        if self.staff:
            _dict['staff'] = self.staff.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_status
        if self.sub_status:
            _dict['subStatus'] = self.sub_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transfer_to_office
        if self.transfer_to_office:
            _dict['transferToOffice'] = self.transfer_to_office.to_dict()
        # override the default output from pydantic by calling `to_dict()` of withdrawal_reason
        if self.withdrawal_reason:
            _dict['withdrawalReason'] = self.withdrawal_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of withdrawn_by
        if self.withdrawn_by:
            _dict['withdrawnBy'] = self.withdrawn_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Client from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountNumber": obj.get("accountNumber"),
            "accountNumberRequiresAutoGeneration": obj.get("accountNumberRequiresAutoGeneration"),
            "activatedBy": AppUser.from_dict(obj["activatedBy"]) if obj.get("activatedBy") is not None else None,
            "activationDate": obj.get("activationDate"),
            "active": obj.get("active"),
            "clientClassification": CodeValue.from_dict(obj["clientClassification"]) if obj.get("clientClassification") is not None else None,
            "clientType": CodeValue.from_dict(obj["clientType"]) if obj.get("clientType") is not None else None,
            "closed": obj.get("closed"),
            "closedBy": AppUser.from_dict(obj["closedBy"]) if obj.get("closedBy") is not None else None,
            "closureDate": obj.get("closureDate"),
            "closureReason": CodeValue.from_dict(obj["closureReason"]) if obj.get("closureReason") is not None else None,
            "createdBy": obj.get("createdBy"),
            "createdDate": obj.get("createdDate"),
            "createdDateTime": obj.get("createdDateTime"),
            "dateOfBirth": obj.get("dateOfBirth"),
            "displayName": obj.get("displayName"),
            "emailAddress": obj.get("emailAddress"),
            "externalId": ExternalId.from_dict(obj["externalId"]) if obj.get("externalId") is not None else None,
            "firstname": obj.get("firstname"),
            "fullname": obj.get("fullname"),
            "gender": CodeValue.from_dict(obj["gender"]) if obj.get("gender") is not None else None,
            "groups": [Group.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "id": obj.get("id"),
            "identifiers": [ClientIdentifier.from_dict(_item) for _item in obj["identifiers"]] if obj.get("identifiers") is not None else None,
            "image": Image.from_dict(obj["image"]) if obj.get("image") is not None else None,
            "lastModifiedBy": obj.get("lastModifiedBy"),
            "lastModifiedDate": obj.get("lastModifiedDate"),
            "lastModifiedDateTime": obj.get("lastModifiedDateTime"),
            "lastname": obj.get("lastname"),
            "legalForm": obj.get("legalForm"),
            "middlename": obj.get("middlename"),
            "mobileNo": obj.get("mobileNo"),
            "new": obj.get("new"),
            "notActive": obj.get("notActive"),
            "notPending": obj.get("notPending"),
            "notStaff": obj.get("notStaff"),
            "office": Office.from_dict(obj["office"]) if obj.get("office") is not None else None,
            "officeJoiningDate": obj.get("officeJoiningDate"),
            "pending": obj.get("pending"),
            "proposedTransferDate": obj.get("proposedTransferDate"),
            "reactivateDate": obj.get("reactivateDate"),
            "reactivatedBy": AppUser.from_dict(obj["reactivatedBy"]) if obj.get("reactivatedBy") is not None else None,
            "rejected": obj.get("rejected"),
            "rejectedBy": AppUser.from_dict(obj["rejectedBy"]) if obj.get("rejectedBy") is not None else None,
            "rejectedDate": obj.get("rejectedDate"),
            "rejectionDate": obj.get("rejectionDate"),
            "rejectionReason": CodeValue.from_dict(obj["rejectionReason"]) if obj.get("rejectionReason") is not None else None,
            "reopenedBy": AppUser.from_dict(obj["reopenedBy"]) if obj.get("reopenedBy") is not None else None,
            "reopenedDate": obj.get("reopenedDate"),
            "savingsAccountId": obj.get("savingsAccountId"),
            "savingsProductId": obj.get("savingsProductId"),
            "staff": Staff.from_dict(obj["staff"]) if obj.get("staff") is not None else None,
            "status": obj.get("status"),
            "subStatus": CodeValue.from_dict(obj["subStatus"]) if obj.get("subStatus") is not None else None,
            "submittedOnDate": obj.get("submittedOnDate"),
            "transferInProgress": obj.get("transferInProgress"),
            "transferInProgressOrOnHold": obj.get("transferInProgressOrOnHold"),
            "transferOnHold": obj.get("transferOnHold"),
            "transferToOffice": Office.from_dict(obj["transferToOffice"]) if obj.get("transferToOffice") is not None else None,
            "withdrawalDate": obj.get("withdrawalDate"),
            "withdrawalReason": CodeValue.from_dict(obj["withdrawalReason"]) if obj.get("withdrawalReason") is not None else None,
            "withdrawn": obj.get("withdrawn"),
            "withdrawnBy": AppUser.from_dict(obj["withdrawnBy"]) if obj.get("withdrawnBy") is not None else None
        })
        return _obj

from fineract_client.models.app_user import AppUser
from fineract_client.models.group import Group
# TODO: Rewrite to not use raise_errors
Client.model_rebuild(raise_errors=False)

