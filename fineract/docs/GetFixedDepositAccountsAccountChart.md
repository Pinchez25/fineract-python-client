# GetFixedDepositAccountsAccountChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_number** | **int** |  | [optional] 
**chart_slabs** | [**List[GetFixedDepositAccountsChartSlabs]**](GetFixedDepositAccountsChartSlabs.md) |  | [optional] 
**from_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**period_types** | [**List[GetFixedDepositAccountsPeriodTypes]**](GetFixedDepositAccountsPeriodTypes.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_accounts_account_chart import GetFixedDepositAccountsAccountChart

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositAccountsAccountChart from a JSON string
get_fixed_deposit_accounts_account_chart_instance = GetFixedDepositAccountsAccountChart.from_json(json)
# print the JSON string representation of the object
print(GetFixedDepositAccountsAccountChart.to_json())

# convert the object into a dict
get_fixed_deposit_accounts_account_chart_dict = get_fixed_deposit_accounts_account_chart_instance.to_dict()
# create an instance of GetFixedDepositAccountsAccountChart from a dict
get_fixed_deposit_accounts_account_chart_from_dict = GetFixedDepositAccountsAccountChart.from_dict(get_fixed_deposit_accounts_account_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


