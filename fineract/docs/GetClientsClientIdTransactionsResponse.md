# GetClientsClientIdTransactionsResponse

GetClientsClientIdTransactionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetClientsPageItems]**](GetClientsPageItems.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_client_id_transactions_response import GetClientsClientIdTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsClientIdTransactionsResponse from a JSON string
get_clients_client_id_transactions_response_instance = GetClientsClientIdTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print GetClientsClientIdTransactionsResponse.to_json()

# convert the object into a dict
get_clients_client_id_transactions_response_dict = get_clients_client_id_transactions_response_instance.to_dict()
# create an instance of GetClientsClientIdTransactionsResponse from a dict
get_clients_client_id_transactions_response_form_dict = get_clients_client_id_transactions_response.from_dict(get_clients_client_id_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


