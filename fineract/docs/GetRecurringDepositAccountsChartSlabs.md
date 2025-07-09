# GetRecurringDepositAccountsChartSlabs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_interest_rate** | **float** |  | [optional] 
**currency** | [**GetRecurringDepositAccountsAccountChartCurrency**](GetRecurringDepositAccountsAccountChartCurrency.md) |  | [optional] 
**from_period** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**period_type** | [**GetRecurringDepositAccountsPeriodType**](GetRecurringDepositAccountsPeriodType.md) |  | [optional] 
**to_period** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_accounts_chart_slabs import GetRecurringDepositAccountsChartSlabs

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositAccountsChartSlabs from a JSON string
get_recurring_deposit_accounts_chart_slabs_instance = GetRecurringDepositAccountsChartSlabs.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositAccountsChartSlabs.to_json()

# convert the object into a dict
get_recurring_deposit_accounts_chart_slabs_dict = get_recurring_deposit_accounts_chart_slabs_instance.to_dict()
# create an instance of GetRecurringDepositAccountsChartSlabs from a dict
get_recurring_deposit_accounts_chart_slabs_form_dict = get_recurring_deposit_accounts_chart_slabs.from_dict(get_recurring_deposit_accounts_chart_slabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


