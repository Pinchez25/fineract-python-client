# GetNotificationsResponse

GetNotificationsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetNotification]**](GetNotification.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_notifications_response import GetNotificationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotificationsResponse from a JSON string
get_notifications_response_instance = GetNotificationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetNotificationsResponse.to_json())

# convert the object into a dict
get_notifications_response_dict = get_notifications_response_instance.to_dict()
# create an instance of GetNotificationsResponse from a dict
get_notifications_response_from_dict = GetNotificationsResponse.from_dict(get_notifications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


