# GetAccountsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**rejected** | **bool** |  | [optional] 
**submitted_and_pending_approval** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_status import GetAccountsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsStatus from a JSON string
get_accounts_status_instance = GetAccountsStatus.from_json(json)
# print the JSON string representation of the object
print(GetAccountsStatus.to_json())

# convert the object into a dict
get_accounts_status_dict = get_accounts_status_instance.to_dict()
# create an instance of GetAccountsStatus from a dict
get_accounts_status_from_dict = GetAccountsStatus.from_dict(get_accounts_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


