# GetAccountTransfersFromOfficeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_from_office_options import GetAccountTransfersFromOfficeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersFromOfficeOptions from a JSON string
get_account_transfers_from_office_options_instance = GetAccountTransfersFromOfficeOptions.from_json(json)
# print the JSON string representation of the object
print(GetAccountTransfersFromOfficeOptions.to_json())

# convert the object into a dict
get_account_transfers_from_office_options_dict = get_account_transfers_from_office_options_instance.to_dict()
# create an instance of GetAccountTransfersFromOfficeOptions from a dict
get_account_transfers_from_office_options_from_dict = GetAccountTransfersFromOfficeOptions.from_dict(get_account_transfers_from_office_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


