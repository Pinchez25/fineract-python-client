# GetGroupsGroupIdAccountsSavingStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**rejected** | **bool** |  | [optional] 
**submitted_and_pending_approval** | **bool** |  | [optional] 
**withdrawn_by_applicant** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_group_id_accounts_saving_status import GetGroupsGroupIdAccountsSavingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsGroupIdAccountsSavingStatus from a JSON string
get_groups_group_id_accounts_saving_status_instance = GetGroupsGroupIdAccountsSavingStatus.from_json(json)
# print the JSON string representation of the object
print(GetGroupsGroupIdAccountsSavingStatus.to_json())

# convert the object into a dict
get_groups_group_id_accounts_saving_status_dict = get_groups_group_id_accounts_saving_status_instance.to_dict()
# create an instance of GetGroupsGroupIdAccountsSavingStatus from a dict
get_groups_group_id_accounts_saving_status_from_dict = GetGroupsGroupIdAccountsSavingStatus.from_dict(get_groups_group_id_accounts_saving_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


