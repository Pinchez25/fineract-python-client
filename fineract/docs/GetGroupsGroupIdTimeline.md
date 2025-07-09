# GetGroupsGroupIdTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_by_firstname** | **str** |  | [optional] 
**activated_by_lastname** | **str** |  | [optional] 
**activated_by_username** | **str** |  | [optional] 
**activated_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_group_id_timeline import GetGroupsGroupIdTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsGroupIdTimeline from a JSON string
get_groups_group_id_timeline_instance = GetGroupsGroupIdTimeline.from_json(json)
# print the JSON string representation of the object
print GetGroupsGroupIdTimeline.to_json()

# convert the object into a dict
get_groups_group_id_timeline_dict = get_groups_group_id_timeline_instance.to_dict()
# create an instance of GetGroupsGroupIdTimeline from a dict
get_groups_group_id_timeline_form_dict = get_groups_group_id_timeline.from_dict(get_groups_group_id_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


