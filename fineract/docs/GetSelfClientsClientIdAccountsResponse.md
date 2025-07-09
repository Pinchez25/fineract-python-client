# GetSelfClientsClientIdAccountsResponse

GetSelfClientsClientIdAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_accounts** | [**List[GetSelfClientsLoanAccounts]**](GetSelfClientsLoanAccounts.md) |  | [optional] 
**savings_accounts** | [**List[GetSelfClientsSavingsAccounts]**](GetSelfClientsSavingsAccounts.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_client_id_accounts_response import GetSelfClientsClientIdAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsClientIdAccountsResponse from a JSON string
get_self_clients_client_id_accounts_response_instance = GetSelfClientsClientIdAccountsResponse.from_json(json)
# print the JSON string representation of the object
print GetSelfClientsClientIdAccountsResponse.to_json()

# convert the object into a dict
get_self_clients_client_id_accounts_response_dict = get_self_clients_client_id_accounts_response_instance.to_dict()
# create an instance of GetSelfClientsClientIdAccountsResponse from a dict
get_self_clients_client_id_accounts_response_form_dict = get_self_clients_client_id_accounts_response.from_dict(get_self_clients_client_id_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


