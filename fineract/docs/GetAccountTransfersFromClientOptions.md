# GetAccountTransfersFromClientOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_from_client_options import GetAccountTransfersFromClientOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersFromClientOptions from a JSON string
get_account_transfers_from_client_options_instance = GetAccountTransfersFromClientOptions.from_json(json)
# print the JSON string representation of the object
print(GetAccountTransfersFromClientOptions.to_json())

# convert the object into a dict
get_account_transfers_from_client_options_dict = get_account_transfers_from_client_options_instance.to_dict()
# create an instance of GetAccountTransfersFromClientOptions from a dict
get_account_transfers_from_client_options_from_dict = GetAccountTransfersFromClientOptions.from_dict(get_account_transfers_from_client_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


