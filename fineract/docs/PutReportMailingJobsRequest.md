# PutReportMailingJobsRequest

PutReportMailingJobsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**start_date_time** | **datetime** |  | [optional] 

## Example

```python
from fineract_client.models.put_report_mailing_jobs_request import PutReportMailingJobsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutReportMailingJobsRequest from a JSON string
put_report_mailing_jobs_request_instance = PutReportMailingJobsRequest.from_json(json)
# print the JSON string representation of the object
print PutReportMailingJobsRequest.to_json()

# convert the object into a dict
put_report_mailing_jobs_request_dict = put_report_mailing_jobs_request_instance.to_dict()
# create an instance of PutReportMailingJobsRequest from a dict
put_report_mailing_jobs_request_form_dict = put_report_mailing_jobs_request.from_dict(put_report_mailing_jobs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


