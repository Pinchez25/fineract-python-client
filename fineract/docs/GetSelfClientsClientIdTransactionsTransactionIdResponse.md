# GetSelfClientsClientIdTransactionsTransactionIdResponse

GetSelfClientsClientIdTransactionsTransactionIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | [**GetSelfClientsSavingsAccountsCurrency**](GetSelfClientsSavingsAccountsCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**reversed** | **bool** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**type** | [**GetSelfClientsClientIdTransactionsType**](GetSelfClientsClientIdTransactionsType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_client_id_transactions_transaction_id_response import GetSelfClientsClientIdTransactionsTransactionIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsClientIdTransactionsTransactionIdResponse from a JSON string
get_self_clients_client_id_transactions_transaction_id_response_instance = GetSelfClientsClientIdTransactionsTransactionIdResponse.from_json(json)
# print the JSON string representation of the object
print GetSelfClientsClientIdTransactionsTransactionIdResponse.to_json()

# convert the object into a dict
get_self_clients_client_id_transactions_transaction_id_response_dict = get_self_clients_client_id_transactions_transaction_id_response_instance.to_dict()
# create an instance of GetSelfClientsClientIdTransactionsTransactionIdResponse from a dict
get_self_clients_client_id_transactions_transaction_id_response_form_dict = get_self_clients_client_id_transactions_transaction_id_response.from_dict(get_self_clients_client_id_transactions_transaction_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


