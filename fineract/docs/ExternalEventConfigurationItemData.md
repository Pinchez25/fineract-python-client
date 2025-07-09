# ExternalEventConfigurationItemData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.external_event_configuration_item_data import ExternalEventConfigurationItemData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalEventConfigurationItemData from a JSON string
external_event_configuration_item_data_instance = ExternalEventConfigurationItemData.from_json(json)
# print the JSON string representation of the object
print(ExternalEventConfigurationItemData.to_json())

# convert the object into a dict
external_event_configuration_item_data_dict = external_event_configuration_item_data_instance.to_dict()
# create an instance of ExternalEventConfigurationItemData from a dict
external_event_configuration_item_data_from_dict = ExternalEventConfigurationItemData.from_dict(external_event_configuration_item_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


