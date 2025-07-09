# ExternalServicesPropertiesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.external_services_properties_data import ExternalServicesPropertiesData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalServicesPropertiesData from a JSON string
external_services_properties_data_instance = ExternalServicesPropertiesData.from_json(json)
# print the JSON string representation of the object
print(ExternalServicesPropertiesData.to_json())

# convert the object into a dict
external_services_properties_data_dict = external_services_properties_data_instance.to_dict()
# create an instance of ExternalServicesPropertiesData from a dict
external_services_properties_data_from_dict = ExternalServicesPropertiesData.from_dict(external_services_properties_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


