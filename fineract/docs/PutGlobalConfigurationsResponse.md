# PutGlobalConfigurationsResponse

PutGlobalConfigurationsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutGlobalConfigurationsResponsechangesSwagger**](PutGlobalConfigurationsResponsechangesSwagger.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_global_configurations_response import PutGlobalConfigurationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutGlobalConfigurationsResponse from a JSON string
put_global_configurations_response_instance = PutGlobalConfigurationsResponse.from_json(json)
# print the JSON string representation of the object
print(PutGlobalConfigurationsResponse.to_json())

# convert the object into a dict
put_global_configurations_response_dict = put_global_configurations_response_instance.to_dict()
# create an instance of PutGlobalConfigurationsResponse from a dict
put_global_configurations_response_from_dict = PutGlobalConfigurationsResponse.from_dict(put_global_configurations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


