# GetNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**actor_id** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_read** | **bool** |  | [optional] 
**is_system_generated** | **bool** |  | [optional] 
**object_id** | **int** |  | [optional] 
**object_type** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**tenant_identifier** | **str** |  | [optional] 
**user_ids** | **List[int]** |  | [optional] 

## Example

```python
from fineract_client.models.get_notification import GetNotification

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotification from a JSON string
get_notification_instance = GetNotification.from_json(json)
# print the JSON string representation of the object
print(GetNotification.to_json())

# convert the object into a dict
get_notification_dict = get_notification_instance.to_dict()
# create an instance of GetNotification from a dict
get_notification_from_dict = GetNotification.from_dict(get_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


