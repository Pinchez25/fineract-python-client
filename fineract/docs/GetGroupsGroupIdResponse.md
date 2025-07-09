# GetGroupsGroupIdResponse

GetGroupsGroupIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**timeline** | [**GetGroupsGroupIdTimeline**](GetGroupsGroupIdTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_group_id_response import GetGroupsGroupIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsGroupIdResponse from a JSON string
get_groups_group_id_response_instance = GetGroupsGroupIdResponse.from_json(json)
# print the JSON string representation of the object
print GetGroupsGroupIdResponse.to_json()

# convert the object into a dict
get_groups_group_id_response_dict = get_groups_group_id_response_instance.to_dict()
# create an instance of GetGroupsGroupIdResponse from a dict
get_groups_group_id_response_form_dict = get_groups_group_id_response.from_dict(get_groups_group_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


