# ClientTimelineData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_by_firstname** | **str** |  | [optional] 
**activated_by_lastname** | **str** |  | [optional] 
**activated_by_username** | **str** |  | [optional] 
**activated_on_date** | **date** |  | [optional] 
**closed_by_firstname** | **str** |  | [optional] 
**closed_by_lastname** | **str** |  | [optional] 
**closed_by_username** | **str** |  | [optional] 
**closed_on_date** | **date** |  | [optional] 
**submitted_by_firstname** | **str** |  | [optional] 
**submitted_by_lastname** | **str** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.client_timeline_data import ClientTimelineData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientTimelineData from a JSON string
client_timeline_data_instance = ClientTimelineData.from_json(json)
# print the JSON string representation of the object
print(ClientTimelineData.to_json())

# convert the object into a dict
client_timeline_data_dict = client_timeline_data_instance.to_dict()
# create an instance of ClientTimelineData from a dict
client_timeline_data_from_dict = ClientTimelineData.from_dict(client_timeline_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


