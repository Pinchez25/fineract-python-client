# PutReportMailingJobsResponse

PutReportMailingJobsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutReportMailingJobsResponseChanges**](PutReportMailingJobsResponseChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_report_mailing_jobs_response import PutReportMailingJobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutReportMailingJobsResponse from a JSON string
put_report_mailing_jobs_response_instance = PutReportMailingJobsResponse.from_json(json)
# print the JSON string representation of the object
print(PutReportMailingJobsResponse.to_json())

# convert the object into a dict
put_report_mailing_jobs_response_dict = put_report_mailing_jobs_response_instance.to_dict()
# create an instance of PutReportMailingJobsResponse from a dict
put_report_mailing_jobs_response_from_dict = PutReportMailingJobsResponse.from_dict(put_report_mailing_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


