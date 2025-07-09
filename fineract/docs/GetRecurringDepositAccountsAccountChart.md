# GetRecurringDepositAccountsAccountChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_number** | **int** |  | [optional] 
**chart_slabs** | [**List[GetRecurringDepositAccountsChartSlabs]**](GetRecurringDepositAccountsChartSlabs.md) |  | [optional] 
**from_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**period_types** | [**List[GetRecurringDepositAccountsPeriodTypes]**](GetRecurringDepositAccountsPeriodTypes.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_accounts_account_chart import GetRecurringDepositAccountsAccountChart

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositAccountsAccountChart from a JSON string
get_recurring_deposit_accounts_account_chart_instance = GetRecurringDepositAccountsAccountChart.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositAccountsAccountChart.to_json()

# convert the object into a dict
get_recurring_deposit_accounts_account_chart_dict = get_recurring_deposit_accounts_account_chart_instance.to_dict()
# create an instance of GetRecurringDepositAccountsAccountChart from a dict
get_recurring_deposit_accounts_account_chart_form_dict = get_recurring_deposit_accounts_account_chart.from_dict(get_recurring_deposit_accounts_account_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


