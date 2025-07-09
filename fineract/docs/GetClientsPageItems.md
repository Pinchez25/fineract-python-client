# GetClientsPageItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | [**GetClientTransactionsCurrency**](GetClientTransactionsCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**reversed** | **bool** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**type** | [**GetClientsClientIdTransactionsType**](GetClientsClientIdTransactionsType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_page_items import GetClientsPageItems

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsPageItems from a JSON string
get_clients_page_items_instance = GetClientsPageItems.from_json(json)
# print the JSON string representation of the object
print(GetClientsPageItems.to_json())

# convert the object into a dict
get_clients_page_items_dict = get_clients_page_items_instance.to_dict()
# create an instance of GetClientsPageItems from a dict
get_clients_page_items_from_dict = GetClientsPageItems.from_dict(get_clients_page_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


