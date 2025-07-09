# GetFixedDepositAccountsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**premature_closed** | **bool** |  | [optional] 
**rejected** | **bool** |  | [optional] 
**submitted_and_pending_approval** | **bool** |  | [optional] 
**transfer_in_progress** | **bool** |  | [optional] 
**transfer_on_hold** | **bool** |  | [optional] 
**withdrawn_by_applicant** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_accounts_status import GetFixedDepositAccountsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositAccountsStatus from a JSON string
get_fixed_deposit_accounts_status_instance = GetFixedDepositAccountsStatus.from_json(json)
# print the JSON string representation of the object
print(GetFixedDepositAccountsStatus.to_json())

# convert the object into a dict
get_fixed_deposit_accounts_status_dict = get_fixed_deposit_accounts_status_instance.to_dict()
# create an instance of GetFixedDepositAccountsStatus from a dict
get_fixed_deposit_accounts_status_from_dict = GetFixedDepositAccountsStatus.from_dict(get_fixed_deposit_accounts_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


