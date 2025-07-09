# GetClientsClientIdAccountsResponse

GetClientsClientIdAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_accounts** | [**List[GetClientsLoanAccounts]**](GetClientsLoanAccounts.md) |  | [optional] 
**savings_accounts** | [**List[GetClientsSavingsAccounts]**](GetClientsSavingsAccounts.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_client_id_accounts_response import GetClientsClientIdAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsClientIdAccountsResponse from a JSON string
get_clients_client_id_accounts_response_instance = GetClientsClientIdAccountsResponse.from_json(json)
# print the JSON string representation of the object
print GetClientsClientIdAccountsResponse.to_json()

# convert the object into a dict
get_clients_client_id_accounts_response_dict = get_clients_client_id_accounts_response_instance.to_dict()
# create an instance of GetClientsClientIdAccountsResponse from a dict
get_clients_client_id_accounts_response_form_dict = get_clients_client_id_accounts_response.from_dict(get_clients_client_id_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


