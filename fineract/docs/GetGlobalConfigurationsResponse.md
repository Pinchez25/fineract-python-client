# GetGlobalConfigurationsResponse

GetGlobalConfigurationsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_configuration** | [**List[GlobalConfigurationPropertyData]**](GlobalConfigurationPropertyData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_global_configurations_response import GetGlobalConfigurationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlobalConfigurationsResponse from a JSON string
get_global_configurations_response_instance = GetGlobalConfigurationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetGlobalConfigurationsResponse.to_json())

# convert the object into a dict
get_global_configurations_response_dict = get_global_configurations_response_instance.to_dict()
# create an instance of GetGlobalConfigurationsResponse from a dict
get_global_configurations_response_from_dict = GetGlobalConfigurationsResponse.from_dict(get_global_configurations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


