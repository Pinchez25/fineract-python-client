# GetClientsSavingsAccountsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**matured** | **bool** |  | [optional] 
**premature_closed** | **bool** |  | [optional] 
**rejected** | **bool** |  | [optional] 
**submitted_and_pending_approval** | **bool** |  | [optional] 
**transfer_in_progress** | **bool** |  | [optional] 
**transfer_on_hold** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**withdrawn_by_applicant** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_savings_accounts_status import GetClientsSavingsAccountsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsSavingsAccountsStatus from a JSON string
get_clients_savings_accounts_status_instance = GetClientsSavingsAccountsStatus.from_json(json)
# print the JSON string representation of the object
print(GetClientsSavingsAccountsStatus.to_json())

# convert the object into a dict
get_clients_savings_accounts_status_dict = get_clients_savings_accounts_status_instance.to_dict()
# create an instance of GetClientsSavingsAccountsStatus from a dict
get_clients_savings_accounts_status_from_dict = GetClientsSavingsAccountsStatus.from_dict(get_clients_savings_accounts_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


