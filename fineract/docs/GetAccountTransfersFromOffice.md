# GetAccountTransfersFromOffice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 
**opening_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_from_office import GetAccountTransfersFromOffice

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersFromOffice from a JSON string
get_account_transfers_from_office_instance = GetAccountTransfersFromOffice.from_json(json)
# print the JSON string representation of the object
print(GetAccountTransfersFromOffice.to_json())

# convert the object into a dict
get_account_transfers_from_office_dict = get_account_transfers_from_office_instance.to_dict()
# create an instance of GetAccountTransfersFromOffice from a dict
get_account_transfers_from_office_from_dict = GetAccountTransfersFromOffice.from_dict(get_account_transfers_from_office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


