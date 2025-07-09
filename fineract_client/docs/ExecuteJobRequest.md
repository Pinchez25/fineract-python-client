# ExecuteJobRequest

ExecuteJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_parameters** | [**List[JobParameterDTO]**](JobParameterDTO.md) |  | [optional] 

## Example

```python
from fineract_client.models.execute_job_request import ExecuteJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteJobRequest from a JSON string
execute_job_request_instance = ExecuteJobRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteJobRequest.to_json())

# convert the object into a dict
execute_job_request_dict = execute_job_request_instance.to_dict()
# create an instance of ExecuteJobRequest from a dict
execute_job_request_from_dict = ExecuteJobRequest.from_dict(execute_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


