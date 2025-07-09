# GetGroupsGroupIdAccountsLoanType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_group_id_accounts_loan_type import GetGroupsGroupIdAccountsLoanType

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsGroupIdAccountsLoanType from a JSON string
get_groups_group_id_accounts_loan_type_instance = GetGroupsGroupIdAccountsLoanType.from_json(json)
# print the JSON string representation of the object
print(GetGroupsGroupIdAccountsLoanType.to_json())

# convert the object into a dict
get_groups_group_id_accounts_loan_type_dict = get_groups_group_id_accounts_loan_type_instance.to_dict()
# create an instance of GetGroupsGroupIdAccountsLoanType from a dict
get_groups_group_id_accounts_loan_type_from_dict = GetGroupsGroupIdAccountsLoanType.from_dict(get_groups_group_id_accounts_loan_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


