# GetClientsLoanAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**currency** | [**GetClientsLoansAccountsCurrency**](GetClientsLoansAccountsCurrency.md) |  | [optional] 
**external_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**loan_cycle** | **int** |  | [optional] 
**loan_type** | [**GetClientsLoanAccountsType**](GetClientsLoanAccountsType.md) |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**short_product_name** | **str** |  | [optional] 
**status** | [**GetClientsLoanAccountsStatus**](GetClientsLoanAccountsStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_loan_accounts import GetClientsLoanAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsLoanAccounts from a JSON string
get_clients_loan_accounts_instance = GetClientsLoanAccounts.from_json(json)
# print the JSON string representation of the object
print(GetClientsLoanAccounts.to_json())

# convert the object into a dict
get_clients_loan_accounts_dict = get_clients_loan_accounts_instance.to_dict()
# create an instance of GetClientsLoanAccounts from a dict
get_clients_loan_accounts_from_dict = GetClientsLoanAccounts.from_dict(get_clients_loan_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


