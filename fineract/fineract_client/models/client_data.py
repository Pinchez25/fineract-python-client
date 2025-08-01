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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fineract_client.models.client_collateral_management_data import ClientCollateralManagementData
from fineract_client.models.client_family_members_data import ClientFamilyMembersData
from fineract_client.models.client_timeline_data import ClientTimelineData
from fineract_client.models.code_value_data import CodeValueData
from fineract_client.models.datatable_data import DatatableData
from fineract_client.models.enum_option_data import EnumOptionData
from fineract_client.models.external_id import ExternalId
from fineract_client.models.office_data import OfficeData
from fineract_client.models.savings_product_data import SavingsProductData
from fineract_client.models.staff_data import StaffData
from typing import Optional, Set
from typing_extensions import Self

class ClientData(BaseModel):
    """
    ClientData
    """ # noqa: E501
    account_no: Optional[StrictStr] = Field(default=None, alias="accountNo")
    activation_date: Optional[date] = Field(default=None, alias="activationDate")
    active: Optional[StrictBool] = None
    address: Optional[List[Dict[str, Any]]] = None
    client_classification: Optional[CodeValueData] = Field(default=None, alias="clientClassification")
    client_classification_id: Optional[StrictInt] = Field(default=None, alias="clientClassificationId")
    client_classification_options: Optional[List[CodeValueData]] = Field(default=None, alias="clientClassificationOptions")
    client_collateral_managements: Optional[List[ClientCollateralManagementData]] = Field(default=None, alias="clientCollateralManagements")
    client_legal_form_options: Optional[List[EnumOptionData]] = Field(default=None, alias="clientLegalFormOptions")
    client_non_person_constitution_options: Optional[List[CodeValueData]] = Field(default=None, alias="clientNonPersonConstitutionOptions")
    client_non_person_details: Optional[Dict[str, Any]] = Field(default=None, alias="clientNonPersonDetails")
    client_non_person_main_business_line_options: Optional[List[CodeValueData]] = Field(default=None, alias="clientNonPersonMainBusinessLineOptions")
    client_type: Optional[CodeValueData] = Field(default=None, alias="clientType")
    client_type_id: Optional[StrictInt] = Field(default=None, alias="clientTypeId")
    client_type_options: Optional[List[CodeValueData]] = Field(default=None, alias="clientTypeOptions")
    datatables: Optional[List[DatatableData]] = None
    date_format: Optional[StrictStr] = Field(default=None, alias="dateFormat")
    date_of_birth: Optional[date] = Field(default=None, alias="dateOfBirth")
    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    email_address: Optional[StrictStr] = Field(default=None, alias="emailAddress")
    external_id: Optional[ExternalId] = Field(default=None, alias="externalId")
    family_member_options: Optional[ClientFamilyMembersData] = Field(default=None, alias="familyMemberOptions")
    firstname: Optional[StrictStr] = None
    fullname: Optional[StrictStr] = None
    gender: Optional[CodeValueData] = None
    gender_id: Optional[StrictInt] = Field(default=None, alias="genderId")
    gender_options: Optional[List[CodeValueData]] = Field(default=None, alias="genderOptions")
    groups: Optional[List[GroupGeneralData]] = None
    id: Optional[StrictInt] = None
    image_id: Optional[StrictInt] = Field(default=None, alias="imageId")
    image_present: Optional[StrictBool] = Field(default=None, alias="imagePresent")
    is_address_enabled: Optional[StrictBool] = Field(default=None, alias="isAddressEnabled")
    is_staff: Optional[StrictBool] = Field(default=None, alias="isStaff")
    lastname: Optional[StrictStr] = None
    legal_form: Optional[EnumOptionData] = Field(default=None, alias="legalForm")
    legal_form_id: Optional[StrictInt] = Field(default=None, alias="legalFormId")
    locale: Optional[StrictStr] = None
    middlename: Optional[StrictStr] = None
    mobile_no: Optional[StrictStr] = Field(default=None, alias="mobileNo")
    narrations: Optional[List[CodeValueData]] = None
    office_id: Optional[StrictInt] = Field(default=None, alias="officeId")
    office_name: Optional[StrictStr] = Field(default=None, alias="officeName")
    office_options: Optional[List[OfficeData]] = Field(default=None, alias="officeOptions")
    row_index: Optional[StrictInt] = Field(default=None, alias="rowIndex")
    saving_account_options: Optional[List[SavingsAccountData]] = Field(default=None, alias="savingAccountOptions")
    saving_product_options: Optional[List[SavingsProductData]] = Field(default=None, alias="savingProductOptions")
    savings_account_id: Optional[StrictInt] = Field(default=None, alias="savingsAccountId")
    savings_product_id: Optional[StrictInt] = Field(default=None, alias="savingsProductId")
    savings_product_name: Optional[StrictStr] = Field(default=None, alias="savingsProductName")
    staff_id: Optional[StrictInt] = Field(default=None, alias="staffId")
    staff_name: Optional[StrictStr] = Field(default=None, alias="staffName")
    staff_options: Optional[List[StaffData]] = Field(default=None, alias="staffOptions")
    status: Optional[EnumOptionData] = None
    sub_status: Optional[CodeValueData] = Field(default=None, alias="subStatus")
    submitted_on_date: Optional[date] = Field(default=None, alias="submittedOnDate")
    timeline: Optional[ClientTimelineData] = None
    transfer_to_office_id: Optional[StrictInt] = Field(default=None, alias="transferToOfficeId")
    transfer_to_office_name: Optional[StrictStr] = Field(default=None, alias="transferToOfficeName")
    __properties: ClassVar[List[str]] = ["accountNo", "activationDate", "active", "address", "clientClassification", "clientClassificationId", "clientClassificationOptions", "clientCollateralManagements", "clientLegalFormOptions", "clientNonPersonConstitutionOptions", "clientNonPersonDetails", "clientNonPersonMainBusinessLineOptions", "clientType", "clientTypeId", "clientTypeOptions", "datatables", "dateFormat", "dateOfBirth", "displayName", "emailAddress", "externalId", "familyMemberOptions", "firstname", "fullname", "gender", "genderId", "genderOptions", "groups", "id", "imageId", "imagePresent", "isAddressEnabled", "isStaff", "lastname", "legalForm", "legalFormId", "locale", "middlename", "mobileNo", "narrations", "officeId", "officeName", "officeOptions", "rowIndex", "savingAccountOptions", "savingProductOptions", "savingsAccountId", "savingsProductId", "savingsProductName", "staffId", "staffName", "staffOptions", "status", "subStatus", "submittedOnDate", "timeline", "transferToOfficeId", "transferToOfficeName"]

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
        """Create an instance of ClientData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of client_classification
        if self.client_classification:
            _dict['clientClassification'] = self.client_classification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in client_classification_options (list)
        _items = []
        if self.client_classification_options:
            for _item_client_classification_options in self.client_classification_options:
                if _item_client_classification_options:
                    _items.append(_item_client_classification_options.to_dict())
            _dict['clientClassificationOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in client_collateral_managements (list)
        _items = []
        if self.client_collateral_managements:
            for _item_client_collateral_managements in self.client_collateral_managements:
                if _item_client_collateral_managements:
                    _items.append(_item_client_collateral_managements.to_dict())
            _dict['clientCollateralManagements'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in client_legal_form_options (list)
        _items = []
        if self.client_legal_form_options:
            for _item_client_legal_form_options in self.client_legal_form_options:
                if _item_client_legal_form_options:
                    _items.append(_item_client_legal_form_options.to_dict())
            _dict['clientLegalFormOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in client_non_person_constitution_options (list)
        _items = []
        if self.client_non_person_constitution_options:
            for _item_client_non_person_constitution_options in self.client_non_person_constitution_options:
                if _item_client_non_person_constitution_options:
                    _items.append(_item_client_non_person_constitution_options.to_dict())
            _dict['clientNonPersonConstitutionOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in client_non_person_main_business_line_options (list)
        _items = []
        if self.client_non_person_main_business_line_options:
            for _item_client_non_person_main_business_line_options in self.client_non_person_main_business_line_options:
                if _item_client_non_person_main_business_line_options:
                    _items.append(_item_client_non_person_main_business_line_options.to_dict())
            _dict['clientNonPersonMainBusinessLineOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of client_type
        if self.client_type:
            _dict['clientType'] = self.client_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in client_type_options (list)
        _items = []
        if self.client_type_options:
            for _item_client_type_options in self.client_type_options:
                if _item_client_type_options:
                    _items.append(_item_client_type_options.to_dict())
            _dict['clientTypeOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in datatables (list)
        _items = []
        if self.datatables:
            for _item_datatables in self.datatables:
                if _item_datatables:
                    _items.append(_item_datatables.to_dict())
            _dict['datatables'] = _items
        # override the default output from pydantic by calling `to_dict()` of external_id
        if self.external_id:
            _dict['externalId'] = self.external_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of family_member_options
        if self.family_member_options:
            _dict['familyMemberOptions'] = self.family_member_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gender
        if self.gender:
            _dict['gender'] = self.gender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in gender_options (list)
        _items = []
        if self.gender_options:
            for _item_gender_options in self.gender_options:
                if _item_gender_options:
                    _items.append(_item_gender_options.to_dict())
            _dict['genderOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of legal_form
        if self.legal_form:
            _dict['legalForm'] = self.legal_form.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in narrations (list)
        _items = []
        if self.narrations:
            for _item_narrations in self.narrations:
                if _item_narrations:
                    _items.append(_item_narrations.to_dict())
            _dict['narrations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in office_options (list)
        _items = []
        if self.office_options:
            for _item_office_options in self.office_options:
                if _item_office_options:
                    _items.append(_item_office_options.to_dict())
            _dict['officeOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in saving_account_options (list)
        _items = []
        if self.saving_account_options:
            for _item_saving_account_options in self.saving_account_options:
                if _item_saving_account_options:
                    _items.append(_item_saving_account_options.to_dict())
            _dict['savingAccountOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in saving_product_options (list)
        _items = []
        if self.saving_product_options:
            for _item_saving_product_options in self.saving_product_options:
                if _item_saving_product_options:
                    _items.append(_item_saving_product_options.to_dict())
            _dict['savingProductOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in staff_options (list)
        _items = []
        if self.staff_options:
            for _item_staff_options in self.staff_options:
                if _item_staff_options:
                    _items.append(_item_staff_options.to_dict())
            _dict['staffOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_status
        if self.sub_status:
            _dict['subStatus'] = self.sub_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timeline
        if self.timeline:
            _dict['timeline'] = self.timeline.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountNo": obj.get("accountNo"),
            "activationDate": obj.get("activationDate"),
            "active": obj.get("active"),
            "address": obj.get("address"),
            "clientClassification": CodeValueData.from_dict(obj["clientClassification"]) if obj.get("clientClassification") is not None else None,
            "clientClassificationId": obj.get("clientClassificationId"),
            "clientClassificationOptions": [CodeValueData.from_dict(_item) for _item in obj["clientClassificationOptions"]] if obj.get("clientClassificationOptions") is not None else None,
            "clientCollateralManagements": [ClientCollateralManagementData.from_dict(_item) for _item in obj["clientCollateralManagements"]] if obj.get("clientCollateralManagements") is not None else None,
            "clientLegalFormOptions": [EnumOptionData.from_dict(_item) for _item in obj["clientLegalFormOptions"]] if obj.get("clientLegalFormOptions") is not None else None,
            "clientNonPersonConstitutionOptions": [CodeValueData.from_dict(_item) for _item in obj["clientNonPersonConstitutionOptions"]] if obj.get("clientNonPersonConstitutionOptions") is not None else None,
            "clientNonPersonDetails": obj.get("clientNonPersonDetails"),
            "clientNonPersonMainBusinessLineOptions": [CodeValueData.from_dict(_item) for _item in obj["clientNonPersonMainBusinessLineOptions"]] if obj.get("clientNonPersonMainBusinessLineOptions") is not None else None,
            "clientType": CodeValueData.from_dict(obj["clientType"]) if obj.get("clientType") is not None else None,
            "clientTypeId": obj.get("clientTypeId"),
            "clientTypeOptions": [CodeValueData.from_dict(_item) for _item in obj["clientTypeOptions"]] if obj.get("clientTypeOptions") is not None else None,
            "datatables": [DatatableData.from_dict(_item) for _item in obj["datatables"]] if obj.get("datatables") is not None else None,
            "dateFormat": obj.get("dateFormat"),
            "dateOfBirth": obj.get("dateOfBirth"),
            "displayName": obj.get("displayName"),
            "emailAddress": obj.get("emailAddress"),
            "externalId": ExternalId.from_dict(obj["externalId"]) if obj.get("externalId") is not None else None,
            "familyMemberOptions": ClientFamilyMembersData.from_dict(obj["familyMemberOptions"]) if obj.get("familyMemberOptions") is not None else None,
            "firstname": obj.get("firstname"),
            "fullname": obj.get("fullname"),
            "gender": CodeValueData.from_dict(obj["gender"]) if obj.get("gender") is not None else None,
            "genderId": obj.get("genderId"),
            "genderOptions": [CodeValueData.from_dict(_item) for _item in obj["genderOptions"]] if obj.get("genderOptions") is not None else None,
            "groups": [GroupGeneralData.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "id": obj.get("id"),
            "imageId": obj.get("imageId"),
            "imagePresent": obj.get("imagePresent"),
            "isAddressEnabled": obj.get("isAddressEnabled"),
            "isStaff": obj.get("isStaff"),
            "lastname": obj.get("lastname"),
            "legalForm": EnumOptionData.from_dict(obj["legalForm"]) if obj.get("legalForm") is not None else None,
            "legalFormId": obj.get("legalFormId"),
            "locale": obj.get("locale"),
            "middlename": obj.get("middlename"),
            "mobileNo": obj.get("mobileNo"),
            "narrations": [CodeValueData.from_dict(_item) for _item in obj["narrations"]] if obj.get("narrations") is not None else None,
            "officeId": obj.get("officeId"),
            "officeName": obj.get("officeName"),
            "officeOptions": [OfficeData.from_dict(_item) for _item in obj["officeOptions"]] if obj.get("officeOptions") is not None else None,
            "rowIndex": obj.get("rowIndex"),
            "savingAccountOptions": [SavingsAccountData.from_dict(_item) for _item in obj["savingAccountOptions"]] if obj.get("savingAccountOptions") is not None else None,
            "savingProductOptions": [SavingsProductData.from_dict(_item) for _item in obj["savingProductOptions"]] if obj.get("savingProductOptions") is not None else None,
            "savingsAccountId": obj.get("savingsAccountId"),
            "savingsProductId": obj.get("savingsProductId"),
            "savingsProductName": obj.get("savingsProductName"),
            "staffId": obj.get("staffId"),
            "staffName": obj.get("staffName"),
            "staffOptions": [StaffData.from_dict(_item) for _item in obj["staffOptions"]] if obj.get("staffOptions") is not None else None,
            "status": EnumOptionData.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "subStatus": CodeValueData.from_dict(obj["subStatus"]) if obj.get("subStatus") is not None else None,
            "submittedOnDate": obj.get("submittedOnDate"),
            "timeline": ClientTimelineData.from_dict(obj["timeline"]) if obj.get("timeline") is not None else None,
            "transferToOfficeId": obj.get("transferToOfficeId"),
            "transferToOfficeName": obj.get("transferToOfficeName")
        })
        return _obj

from fineract_client.models.group_general_data import GroupGeneralData
from fineract_client.models.savings_account_data import SavingsAccountData
# TODO: Rewrite to not use raise_errors
ClientData.model_rebuild(raise_errors=False)

