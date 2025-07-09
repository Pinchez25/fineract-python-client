# GetClientsTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_by_firstname** | **str** |  | [optional] 
**activated_by_lastname** | **str** |  | [optional] 
**activated_by_username** | **str** |  | [optional] 
**activated_on_date** | **date** |  | [optional] 
**submitted_by_firstname** | **str** |  | [optional] 
**submitted_by_lastname** | **str** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_timeline import GetClientsTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsTimeline from a JSON string
get_clients_timeline_instance = GetClientsTimeline.from_json(json)
# print the JSON string representation of the object
print(GetClientsTimeline.to_json())

# convert the object into a dict
get_clients_timeline_dict = get_clients_timeline_instance.to_dict()
# create an instance of GetClientsTimeline from a dict
get_clients_timeline_from_dict = GetClientsTimeline.from_dict(get_clients_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


