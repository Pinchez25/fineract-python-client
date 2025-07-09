# GetGroupsGroupIdAccountsLoanAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**loan_type** | [**GetGroupsGroupIdAccountsLoanType**](GetGroupsGroupIdAccountsLoanType.md) |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**GetGroupsGroupIdAccountsStatus**](GetGroupsGroupIdAccountsStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_group_id_accounts_loan_accounts import GetGroupsGroupIdAccountsLoanAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsGroupIdAccountsLoanAccounts from a JSON string
get_groups_group_id_accounts_loan_accounts_instance = GetGroupsGroupIdAccountsLoanAccounts.from_json(json)
# print the JSON string representation of the object
print(GetGroupsGroupIdAccountsLoanAccounts.to_json())

# convert the object into a dict
get_groups_group_id_accounts_loan_accounts_dict = get_groups_group_id_accounts_loan_accounts_instance.to_dict()
# create an instance of GetGroupsGroupIdAccountsLoanAccounts from a dict
get_groups_group_id_accounts_loan_accounts_from_dict = GetGroupsGroupIdAccountsLoanAccounts.from_dict(get_groups_group_id_accounts_loan_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


