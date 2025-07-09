# GetGroupsGroupIdAccountsResponse

GetGroupsGroupIdAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_accounts** | [**List[GetGroupsGroupIdAccountsLoanAccounts]**](GetGroupsGroupIdAccountsLoanAccounts.md) |  | [optional] 
**member_loan_accounts** | [**List[GetGroupsGroupIdAccountsMemberLoanAccounts]**](GetGroupsGroupIdAccountsMemberLoanAccounts.md) |  | [optional] 
**member_savings_accounts** | [**List[GetGroupsGroupIdAccountsMemberSavingsAccounts]**](GetGroupsGroupIdAccountsMemberSavingsAccounts.md) |  | [optional] 
**savings_accounts** | [**List[GetGroupsGroupIdAccountsSavingAccounts]**](GetGroupsGroupIdAccountsSavingAccounts.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_group_id_accounts_response import GetGroupsGroupIdAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsGroupIdAccountsResponse from a JSON string
get_groups_group_id_accounts_response_instance = GetGroupsGroupIdAccountsResponse.from_json(json)
# print the JSON string representation of the object
print GetGroupsGroupIdAccountsResponse.to_json()

# convert the object into a dict
get_groups_group_id_accounts_response_dict = get_groups_group_id_accounts_response_instance.to_dict()
# create an instance of GetGroupsGroupIdAccountsResponse from a dict
get_groups_group_id_accounts_response_form_dict = get_groups_group_id_accounts_response.from_dict(get_groups_group_id_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


