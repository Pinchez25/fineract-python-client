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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fineract_client.models.job_detail_history_data import JobDetailHistoryData
from typing import Optional, Set
from typing_extensions import Self

class GetJobsResponse(BaseModel):
    """
    GetJobsResponse
    """ # noqa: E501
    active: Optional[StrictBool] = None
    cron_expression: Optional[StrictStr] = Field(default=None, alias="cronExpression")
    currently_running: Optional[StrictBool] = Field(default=None, alias="currentlyRunning")
    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    initializing_error: Optional[StrictStr] = Field(default=None, alias="initializingError")
    job_id: Optional[StrictInt] = Field(default=None, alias="jobId")
    last_run_history: Optional[JobDetailHistoryData] = Field(default=None, alias="lastRunHistory")
    next_run_time: Optional[datetime] = Field(default=None, alias="nextRunTime")
    __properties: ClassVar[List[str]] = ["active", "cronExpression", "currentlyRunning", "displayName", "initializingError", "jobId", "lastRunHistory", "nextRunTime"]

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
        """Create an instance of GetJobsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of last_run_history
        if self.last_run_history:
            _dict['lastRunHistory'] = self.last_run_history.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetJobsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "cronExpression": obj.get("cronExpression"),
            "currentlyRunning": obj.get("currentlyRunning"),
            "displayName": obj.get("displayName"),
            "initializingError": obj.get("initializingError"),
            "jobId": obj.get("jobId"),
            "lastRunHistory": JobDetailHistoryData.from_dict(obj["lastRunHistory"]) if obj.get("lastRunHistory") is not None else None,
            "nextRunTime": obj.get("nextRunTime")
        })
        return _obj


