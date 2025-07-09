# GetSelfClientsClientIdTransactionsResponse

GetSelfClientsClientIdTransactionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetSelfClientsClientIdTransactionsPageItems]**](GetSelfClientsClientIdTransactionsPageItems.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_client_id_transactions_response import GetSelfClientsClientIdTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsClientIdTransactionsResponse from a JSON string
get_self_clients_client_id_transactions_response_instance = GetSelfClientsClientIdTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSelfClientsClientIdTransactionsResponse.to_json())

# convert the object into a dict
get_self_clients_client_id_transactions_response_dict = get_self_clients_client_id_transactions_response_instance.to_dict()
# create an instance of GetSelfClientsClientIdTransactionsResponse from a dict
get_self_clients_client_id_transactions_response_from_dict = GetSelfClientsClientIdTransactionsResponse.from_dict(get_self_clients_client_id_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


