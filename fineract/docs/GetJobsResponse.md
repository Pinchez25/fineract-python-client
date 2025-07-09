# GetJobsResponse

GetJobsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**cron_expression** | **str** |  | [optional] 
**currently_running** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**initializing_error** | **str** |  | [optional] 
**job_id** | **int** |  | [optional] 
**last_run_history** | [**JobDetailHistoryData**](JobDetailHistoryData.md) |  | [optional] 
**next_run_time** | **datetime** |  | [optional] 

## Example

```python
from fineract_client.models.get_jobs_response import GetJobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetJobsResponse from a JSON string
get_jobs_response_instance = GetJobsResponse.from_json(json)
# print the JSON string representation of the object
print GetJobsResponse.to_json()

# convert the object into a dict
get_jobs_response_dict = get_jobs_response_instance.to_dict()
# create an instance of GetJobsResponse from a dict
get_jobs_response_form_dict = get_jobs_response.from_dict(get_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


