# JobDetailHistoryDataSwagger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_run_end_time** | **datetime** |  | [optional] 
**job_run_start_time** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**trigger_type** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.job_detail_history_data_swagger import JobDetailHistoryDataSwagger

# TODO update the JSON string below
json = "{}"
# create an instance of JobDetailHistoryDataSwagger from a JSON string
job_detail_history_data_swagger_instance = JobDetailHistoryDataSwagger.from_json(json)
# print the JSON string representation of the object
print(JobDetailHistoryDataSwagger.to_json())

# convert the object into a dict
job_detail_history_data_swagger_dict = job_detail_history_data_swagger_instance.to_dict()
# create an instance of JobDetailHistoryDataSwagger from a dict
job_detail_history_data_swagger_from_dict = JobDetailHistoryDataSwagger.from_dict(job_detail_history_data_swagger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


