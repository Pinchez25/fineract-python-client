# GetAccountsLockPeriodTypeEnum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_lock_period_type_enum import GetAccountsLockPeriodTypeEnum

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsLockPeriodTypeEnum from a JSON string
get_accounts_lock_period_type_enum_instance = GetAccountsLockPeriodTypeEnum.from_json(json)
# print the JSON string representation of the object
print(GetAccountsLockPeriodTypeEnum.to_json())

# convert the object into a dict
get_accounts_lock_period_type_enum_dict = get_accounts_lock_period_type_enum_instance.to_dict()
# create an instance of GetAccountsLockPeriodTypeEnum from a dict
get_accounts_lock_period_type_enum_from_dict = GetAccountsLockPeriodTypeEnum.from_dict(get_accounts_lock_period_type_enum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


