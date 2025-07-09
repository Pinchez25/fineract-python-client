# GetGroupsGroupIdAccountsMemberLoanAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**loan_type** | [**GetGroupsGroupIdAccountsMemberLoanType**](GetGroupsGroupIdAccountsMemberLoanType.md) |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**GetGroupsGroupIdAccountsMemberLoanStatus**](GetGroupsGroupIdAccountsMemberLoanStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_group_id_accounts_member_loan_accounts import GetGroupsGroupIdAccountsMemberLoanAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsGroupIdAccountsMemberLoanAccounts from a JSON string
get_groups_group_id_accounts_member_loan_accounts_instance = GetGroupsGroupIdAccountsMemberLoanAccounts.from_json(json)
# print the JSON string representation of the object
print GetGroupsGroupIdAccountsMemberLoanAccounts.to_json()

# convert the object into a dict
get_groups_group_id_accounts_member_loan_accounts_dict = get_groups_group_id_accounts_member_loan_accounts_instance.to_dict()
# create an instance of GetGroupsGroupIdAccountsMemberLoanAccounts from a dict
get_groups_group_id_accounts_member_loan_accounts_form_dict = get_groups_group_id_accounts_member_loan_accounts.from_dict(get_groups_group_id_accounts_member_loan_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


