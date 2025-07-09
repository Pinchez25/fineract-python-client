# GetAccountsTypeStatus


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
from fineract_client.models.get_accounts_type_status import GetAccountsTypeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsTypeStatus from a JSON string
get_accounts_type_status_instance = GetAccountsTypeStatus.from_json(json)
# print the JSON string representation of the object
print GetAccountsTypeStatus.to_json()

# convert the object into a dict
get_accounts_type_status_dict = get_accounts_type_status_instance.to_dict()
# create an instance of GetAccountsTypeStatus from a dict
get_accounts_type_status_form_dict = get_accounts_type_status.from_dict(get_accounts_type_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


