# GlobalConfigurationPropertyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_value** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**string_value** | **str** |  | [optional] 
**trap_door** | **bool** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.global_configuration_property_data import GlobalConfigurationPropertyData

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalConfigurationPropertyData from a JSON string
global_configuration_property_data_instance = GlobalConfigurationPropertyData.from_json(json)
# print the JSON string representation of the object
print GlobalConfigurationPropertyData.to_json()

# convert the object into a dict
global_configuration_property_data_dict = global_configuration_property_data_instance.to_dict()
# create an instance of GlobalConfigurationPropertyData from a dict
global_configuration_property_data_form_dict = global_configuration_property_data.from_dict(global_configuration_property_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


