# GetAccountsLinkedToPocketResponse

GetAccountsLinkedToPocketResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_accounts** | [**List[GetPocketLoanAccounts]**](GetPocketLoanAccounts.md) |  | [optional] 
**saving_accounts** | [**List[GetPocketSavingAccounts]**](GetPocketSavingAccounts.md) |  | [optional] 
**share_accounts** | **List[object]** |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_linked_to_pocket_response import GetAccountsLinkedToPocketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsLinkedToPocketResponse from a JSON string
get_accounts_linked_to_pocket_response_instance = GetAccountsLinkedToPocketResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccountsLinkedToPocketResponse.to_json())

# convert the object into a dict
get_accounts_linked_to_pocket_response_dict = get_accounts_linked_to_pocket_response_instance.to_dict()
# create an instance of GetAccountsLinkedToPocketResponse from a dict
get_accounts_linked_to_pocket_response_from_dict = GetAccountsLinkedToPocketResponse.from_dict(get_accounts_linked_to_pocket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


