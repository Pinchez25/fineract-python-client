# GetAccountTransfersPageItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**GetAccountTransfersPageItemsCurrency**](GetAccountTransfersPageItemsCurrency.md) |  | [optional] 
**from_account** | [**GetAccountTransfersPageItemsFromAccount**](GetAccountTransfersPageItemsFromAccount.md) |  | [optional] 
**from_account_type** | [**GetAccountTransfersFromAccountType**](GetAccountTransfersFromAccountType.md) |  | [optional] 
**from_client** | [**GetAccountTransfersFromClientOptions**](GetAccountTransfersFromClientOptions.md) |  | [optional] 
**from_office** | [**GetAccountTransfersPageItemsFromOffice**](GetAccountTransfersPageItemsFromOffice.md) |  | [optional] 
**id** | **int** |  | [optional] 
**reversed** | **bool** |  | [optional] 
**to_account** | [**GetAccountTransfersPageItemsFromAccount**](GetAccountTransfersPageItemsFromAccount.md) |  | [optional] 
**to_account_type** | [**GetAccountTransfersPageItemsToAccountType**](GetAccountTransfersPageItemsToAccountType.md) |  | [optional] 
**to_client** | [**GetAccountTransfersFromClientOptions**](GetAccountTransfersFromClientOptions.md) |  | [optional] 
**to_office** | [**GetAccountTransfersPageItemsFromOffice**](GetAccountTransfersPageItemsFromOffice.md) |  | [optional] 
**transfer_amount** | **float** |  | [optional] 
**transfer_date** | **date** |  | [optional] 
**transfer_description** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_page_items import GetAccountTransfersPageItems

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersPageItems from a JSON string
get_account_transfers_page_items_instance = GetAccountTransfersPageItems.from_json(json)
# print the JSON string representation of the object
print(GetAccountTransfersPageItems.to_json())

# convert the object into a dict
get_account_transfers_page_items_dict = get_account_transfers_page_items_instance.to_dict()
# create an instance of GetAccountTransfersPageItems from a dict
get_account_transfers_page_items_from_dict = GetAccountTransfersPageItems.from_dict(get_account_transfers_page_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


