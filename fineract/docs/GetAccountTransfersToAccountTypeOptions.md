# GetAccountTransfersToAccountTypeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_to_account_type_options import GetAccountTransfersToAccountTypeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersToAccountTypeOptions from a JSON string
get_account_transfers_to_account_type_options_instance = GetAccountTransfersToAccountTypeOptions.from_json(json)
# print the JSON string representation of the object
print GetAccountTransfersToAccountTypeOptions.to_json()

# convert the object into a dict
get_account_transfers_to_account_type_options_dict = get_account_transfers_to_account_type_options_instance.to_dict()
# create an instance of GetAccountTransfersToAccountTypeOptions from a dict
get_account_transfers_to_account_type_options_form_dict = get_account_transfers_to_account_type_options.from_dict(get_account_transfers_to_account_type_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


