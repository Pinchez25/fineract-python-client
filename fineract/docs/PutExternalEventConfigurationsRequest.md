# PutExternalEventConfigurationsRequest

PutExternalEventConfigurationsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_event_configurations** | **Dict[str, bool]** |  | [optional] 

## Example

```python
from fineract_client.models.put_external_event_configurations_request import PutExternalEventConfigurationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutExternalEventConfigurationsRequest from a JSON string
put_external_event_configurations_request_instance = PutExternalEventConfigurationsRequest.from_json(json)
# print the JSON string representation of the object
print(PutExternalEventConfigurationsRequest.to_json())

# convert the object into a dict
put_external_event_configurations_request_dict = put_external_event_configurations_request_instance.to_dict()
# create an instance of PutExternalEventConfigurationsRequest from a dict
put_external_event_configurations_request_from_dict = PutExternalEventConfigurationsRequest.from_dict(put_external_event_configurations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


