# GetFixedDepositAccountsPeriodTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_accounts_period_types import GetFixedDepositAccountsPeriodTypes

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositAccountsPeriodTypes from a JSON string
get_fixed_deposit_accounts_period_types_instance = GetFixedDepositAccountsPeriodTypes.from_json(json)
# print the JSON string representation of the object
print(GetFixedDepositAccountsPeriodTypes.to_json())

# convert the object into a dict
get_fixed_deposit_accounts_period_types_dict = get_fixed_deposit_accounts_period_types_instance.to_dict()
# create an instance of GetFixedDepositAccountsPeriodTypes from a dict
get_fixed_deposit_accounts_period_types_from_dict = GetFixedDepositAccountsPeriodTypes.from_dict(get_fixed_deposit_accounts_period_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


