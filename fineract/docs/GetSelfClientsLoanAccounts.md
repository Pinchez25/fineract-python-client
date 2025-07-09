# GetSelfClientsLoanAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**external_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**loan_cycle** | **int** |  | [optional] 
**loan_type** | [**GetSelfClientsLoanAccountsType**](GetSelfClientsLoanAccountsType.md) |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**GetSelfClientsLoanAccountsStatus**](GetSelfClientsLoanAccountsStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_loan_accounts import GetSelfClientsLoanAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsLoanAccounts from a JSON string
get_self_clients_loan_accounts_instance = GetSelfClientsLoanAccounts.from_json(json)
# print the JSON string representation of the object
print GetSelfClientsLoanAccounts.to_json()

# convert the object into a dict
get_self_clients_loan_accounts_dict = get_self_clients_loan_accounts_instance.to_dict()
# create an instance of GetSelfClientsLoanAccounts from a dict
get_self_clients_loan_accounts_form_dict = get_self_clients_loan_accounts.from_dict(get_self_clients_loan_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


