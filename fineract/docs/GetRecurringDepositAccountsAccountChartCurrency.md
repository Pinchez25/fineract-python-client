# GetRecurringDepositAccountsAccountChartCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**decimal_places** | **int** |  | [optional] 
**display_label** | **str** |  | [optional] 
**display_symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**name_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_accounts_account_chart_currency import GetRecurringDepositAccountsAccountChartCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositAccountsAccountChartCurrency from a JSON string
get_recurring_deposit_accounts_account_chart_currency_instance = GetRecurringDepositAccountsAccountChartCurrency.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositAccountsAccountChartCurrency.to_json()

# convert the object into a dict
get_recurring_deposit_accounts_account_chart_currency_dict = get_recurring_deposit_accounts_account_chart_currency_instance.to_dict()
# create an instance of GetRecurringDepositAccountsAccountChartCurrency from a dict
get_recurring_deposit_accounts_account_chart_currency_form_dict = get_recurring_deposit_accounts_account_chart_currency.from_dict(get_recurring_deposit_accounts_account_chart_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


