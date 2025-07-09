# GetExternalEventConfigurationsResponse

GetExternalEventConfigurationsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_event_configuration** | [**List[ExternalEventConfigurationItemData]**](ExternalEventConfigurationItemData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_external_event_configurations_response import GetExternalEventConfigurationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExternalEventConfigurationsResponse from a JSON string
get_external_event_configurations_response_instance = GetExternalEventConfigurationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetExternalEventConfigurationsResponse.to_json())

# convert the object into a dict
get_external_event_configurations_response_dict = get_external_event_configurations_response_instance.to_dict()
# create an instance of GetExternalEventConfigurationsResponse from a dict
get_external_event_configurations_response_from_dict = GetExternalEventConfigurationsResponse.from_dict(get_external_event_configurations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


