# GetGroupsGroupIdAccountsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**closed_obligations_met** | **bool** |  | [optional] 
**closed_rescheduled** | **bool** |  | [optional] 
**closed_written_off** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**overpaid** | **bool** |  | [optional] 
**pending_approval** | **bool** |  | [optional] 
**waiting_for_disbursal** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_group_id_accounts_status import GetGroupsGroupIdAccountsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsGroupIdAccountsStatus from a JSON string
get_groups_group_id_accounts_status_instance = GetGroupsGroupIdAccountsStatus.from_json(json)
# print the JSON string representation of the object
print(GetGroupsGroupIdAccountsStatus.to_json())

# convert the object into a dict
get_groups_group_id_accounts_status_dict = get_groups_group_id_accounts_status_instance.to_dict()
# create an instance of GetGroupsGroupIdAccountsStatus from a dict
get_groups_group_id_accounts_status_from_dict = GetGroupsGroupIdAccountsStatus.from_dict(get_groups_group_id_accounts_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


