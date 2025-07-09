# GetFixedDepositAccountsPeriodType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_accounts_period_type import GetFixedDepositAccountsPeriodType

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositAccountsPeriodType from a JSON string
get_fixed_deposit_accounts_period_type_instance = GetFixedDepositAccountsPeriodType.from_json(json)
# print the JSON string representation of the object
print GetFixedDepositAccountsPeriodType.to_json()

# convert the object into a dict
get_fixed_deposit_accounts_period_type_dict = get_fixed_deposit_accounts_period_type_instance.to_dict()
# create an instance of GetFixedDepositAccountsPeriodType from a dict
get_fixed_deposit_accounts_period_type_form_dict = get_fixed_deposit_accounts_period_type.from_dict(get_fixed_deposit_accounts_period_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


