# GetSelfClientsSavingsAccountsStatus


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
**withdrawn_by_applicant** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_savings_accounts_status import GetSelfClientsSavingsAccountsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsSavingsAccountsStatus from a JSON string
get_self_clients_savings_accounts_status_instance = GetSelfClientsSavingsAccountsStatus.from_json(json)
# print the JSON string representation of the object
print(GetSelfClientsSavingsAccountsStatus.to_json())

# convert the object into a dict
get_self_clients_savings_accounts_status_dict = get_self_clients_savings_accounts_status_instance.to_dict()
# create an instance of GetSelfClientsSavingsAccountsStatus from a dict
get_self_clients_savings_accounts_status_from_dict = GetSelfClientsSavingsAccountsStatus.from_dict(get_self_clients_savings_accounts_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


