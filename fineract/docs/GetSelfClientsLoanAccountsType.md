# GetSelfClientsLoanAccountsType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_loan_accounts_type import GetSelfClientsLoanAccountsType

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsLoanAccountsType from a JSON string
get_self_clients_loan_accounts_type_instance = GetSelfClientsLoanAccountsType.from_json(json)
# print the JSON string representation of the object
print(GetSelfClientsLoanAccountsType.to_json())

# convert the object into a dict
get_self_clients_loan_accounts_type_dict = get_self_clients_loan_accounts_type_instance.to_dict()
# create an instance of GetSelfClientsLoanAccountsType from a dict
get_self_clients_loan_accounts_type_from_dict = GetSelfClientsLoanAccountsType.from_dict(get_self_clients_loan_accounts_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


