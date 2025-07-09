# GetGroupsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_status import GetGroupsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsStatus from a JSON string
get_groups_status_instance = GetGroupsStatus.from_json(json)
# print the JSON string representation of the object
print(GetGroupsStatus.to_json())

# convert the object into a dict
get_groups_status_dict = get_groups_status_instance.to_dict()
# create an instance of GetGroupsStatus from a dict
get_groups_status_from_dict = GetGroupsStatus.from_dict(get_groups_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


