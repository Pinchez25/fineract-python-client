# PutGlobalConfigurationsRequest

PutGlobalConfigurationsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**date_value** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**string_value** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_global_configurations_request import PutGlobalConfigurationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutGlobalConfigurationsRequest from a JSON string
put_global_configurations_request_instance = PutGlobalConfigurationsRequest.from_json(json)
# print the JSON string representation of the object
print PutGlobalConfigurationsRequest.to_json()

# convert the object into a dict
put_global_configurations_request_dict = put_global_configurations_request_instance.to_dict()
# create an instance of PutGlobalConfigurationsRequest from a dict
put_global_configurations_request_form_dict = put_global_configurations_request.from_dict(put_global_configurations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


