# GetJobsJobIDJobRunHistoryResponse

GetJobsJobIDJobRunHistoryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[JobDetailHistoryDataSwagger]**](JobDetailHistoryDataSwagger.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_jobs_job_id_job_run_history_response import GetJobsJobIDJobRunHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetJobsJobIDJobRunHistoryResponse from a JSON string
get_jobs_job_id_job_run_history_response_instance = GetJobsJobIDJobRunHistoryResponse.from_json(json)
# print the JSON string representation of the object
print GetJobsJobIDJobRunHistoryResponse.to_json()

# convert the object into a dict
get_jobs_job_id_job_run_history_response_dict = get_jobs_job_id_job_run_history_response_instance.to_dict()
# create an instance of GetJobsJobIDJobRunHistoryResponse from a dict
get_jobs_job_id_job_run_history_response_form_dict = get_jobs_job_id_job_run_history_response.from_dict(get_jobs_job_id_job_run_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


