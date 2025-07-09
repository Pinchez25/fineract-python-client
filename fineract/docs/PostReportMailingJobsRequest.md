# PostReportMailingJobsRequest

PostReportMailingJobsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**email_message** | **str** |  | [optional] 
**email_recipients** | **str** |  | [optional] 
**email_subject** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**start_date_time** | **datetime** |  | [optional] 
**stretchy_report_id** | **int** |  | [optional] 
**stretchy_report_param_map** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_report_mailing_jobs_request import PostReportMailingJobsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostReportMailingJobsRequest from a JSON string
post_report_mailing_jobs_request_instance = PostReportMailingJobsRequest.from_json(json)
# print the JSON string representation of the object
print PostReportMailingJobsRequest.to_json()

# convert the object into a dict
post_report_mailing_jobs_request_dict = post_report_mailing_jobs_request_instance.to_dict()
# create an instance of PostReportMailingJobsRequest from a dict
post_report_mailing_jobs_request_form_dict = post_report_mailing_jobs_request.from_dict(post_report_mailing_jobs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


