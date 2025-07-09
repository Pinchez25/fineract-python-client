# GetAccountTransfersResponse

GetAccountTransfersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetAccountTransfersPageItems]**](GetAccountTransfersPageItems.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_response import GetAccountTransfersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersResponse from a JSON string
get_account_transfers_response_instance = GetAccountTransfersResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccountTransfersResponse.to_json())

# convert the object into a dict
get_account_transfers_response_dict = get_account_transfers_response_instance.to_dict()
# create an instance of GetAccountTransfersResponse from a dict
get_account_transfers_response_from_dict = GetAccountTransfersResponse.from_dict(get_account_transfers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


