# GetClientsLoanAccountsType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_loan_accounts_type import GetClientsLoanAccountsType

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsLoanAccountsType from a JSON string
get_clients_loan_accounts_type_instance = GetClientsLoanAccountsType.from_json(json)
# print the JSON string representation of the object
print(GetClientsLoanAccountsType.to_json())

# convert the object into a dict
get_clients_loan_accounts_type_dict = get_clients_loan_accounts_type_instance.to_dict()
# create an instance of GetClientsLoanAccountsType from a dict
get_clients_loan_accounts_type_from_dict = GetClientsLoanAccountsType.from_dict(get_clients_loan_accounts_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


