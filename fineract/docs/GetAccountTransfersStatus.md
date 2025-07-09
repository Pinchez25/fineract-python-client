# GetAccountTransfersStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_account_transfers_status import GetAccountTransfersStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountTransfersStatus from a JSON string
get_account_transfers_status_instance = GetAccountTransfersStatus.from_json(json)
# print the JSON string representation of the object
print GetAccountTransfersStatus.to_json()

# convert the object into a dict
get_account_transfers_status_dict = get_account_transfers_status_instance.to_dict()
# create an instance of GetAccountTransfersStatus from a dict
get_account_transfers_status_form_dict = get_account_transfers_status.from_dict(get_account_transfers_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


