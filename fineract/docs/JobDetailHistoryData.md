# JobDetailHistoryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_run_end_time** | **datetime** |  | [optional] 
**job_run_error_log** | **str** |  | [optional] 
**job_run_error_message** | **str** |  | [optional] 
**job_run_start_time** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**trigger_type** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.job_detail_history_data import JobDetailHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of JobDetailHistoryData from a JSON string
job_detail_history_data_instance = JobDetailHistoryData.from_json(json)
# print the JSON string representation of the object
print(JobDetailHistoryData.to_json())

# convert the object into a dict
job_detail_history_data_dict = job_detail_history_data_instance.to_dict()
# create an instance of JobDetailHistoryData from a dict
job_detail_history_data_from_dict = JobDetailHistoryData.from_dict(job_detail_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


