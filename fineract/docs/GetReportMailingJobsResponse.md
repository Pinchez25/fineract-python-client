# GetReportMailingJobsResponse

GetReportMailingJobsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**email_attachment_file_format** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**email_message** | **str** |  | [optional] 
**email_recipients** | **str** |  | [optional] 
**email_subject** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**next_run_date_time** | **datetime** |  | [optional] 
**number_of_runs** | **int** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**run_as_user_id** | **int** |  | [optional] 
**start_date_time** | **datetime** |  | [optional] 
**stretchy_report** | **object** |  | [optional] 
**stretchy_report_param_map** | **str** |  | [optional] 
**timeline** | [**ReportMailingJobTimelineData**](ReportMailingJobTimelineData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_report_mailing_jobs_response import GetReportMailingJobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReportMailingJobsResponse from a JSON string
get_report_mailing_jobs_response_instance = GetReportMailingJobsResponse.from_json(json)
# print the JSON string representation of the object
print(GetReportMailingJobsResponse.to_json())

# convert the object into a dict
get_report_mailing_jobs_response_dict = get_report_mailing_jobs_response_instance.to_dict()
# create an instance of GetReportMailingJobsResponse from a dict
get_report_mailing_jobs_response_from_dict = GetReportMailingJobsResponse.from_dict(get_report_mailing_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


