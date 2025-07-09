# GetFixedDepositAccountsChartSlabs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_interest_rate** | **float** |  | [optional] 
**currency** | [**GetFixedDepositAccountsAccountChartCurrency**](GetFixedDepositAccountsAccountChartCurrency.md) |  | [optional] 
**from_period** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**period_type** | [**GetFixedDepositAccountsPeriodType**](GetFixedDepositAccountsPeriodType.md) |  | [optional] 
**to_period** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_accounts_chart_slabs import GetFixedDepositAccountsChartSlabs

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositAccountsChartSlabs from a JSON string
get_fixed_deposit_accounts_chart_slabs_instance = GetFixedDepositAccountsChartSlabs.from_json(json)
# print the JSON string representation of the object
print(GetFixedDepositAccountsChartSlabs.to_json())

# convert the object into a dict
get_fixed_deposit_accounts_chart_slabs_dict = get_fixed_deposit_accounts_chart_slabs_instance.to_dict()
# create an instance of GetFixedDepositAccountsChartSlabs from a dict
get_fixed_deposit_accounts_chart_slabs_from_dict = GetFixedDepositAccountsChartSlabs.from_dict(get_fixed_deposit_accounts_chart_slabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


