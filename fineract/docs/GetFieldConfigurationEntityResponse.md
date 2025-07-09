# GetFieldConfigurationEntityResponse

GetFieldConfigurationEntityResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** |  | [optional] 
**field** | **str** |  | [optional] 
**field_configuration_id** | **int** |  | [optional] 
**is_enabled** | **str** |  | [optional] 
**is_mandatory** | **str** |  | [optional] 
**subentity** | **str** |  | [optional] 
**validation_regex** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_field_configuration_entity_response import GetFieldConfigurationEntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFieldConfigurationEntityResponse from a JSON string
get_field_configuration_entity_response_instance = GetFieldConfigurationEntityResponse.from_json(json)
# print the JSON string representation of the object
print GetFieldConfigurationEntityResponse.to_json()

# convert the object into a dict
get_field_configuration_entity_response_dict = get_field_configuration_entity_response_instance.to_dict()
# create an instance of GetFieldConfigurationEntityResponse from a dict
get_field_configuration_entity_response_form_dict = get_field_configuration_entity_response.from_dict(get_field_configuration_entity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


