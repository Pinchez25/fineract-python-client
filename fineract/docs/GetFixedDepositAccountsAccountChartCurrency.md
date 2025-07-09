# GetFixedDepositAccountsAccountChartCurrency


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
from fineract_client.models.get_fixed_deposit_accounts_account_chart_currency import GetFixedDepositAccountsAccountChartCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositAccountsAccountChartCurrency from a JSON string
get_fixed_deposit_accounts_account_chart_currency_instance = GetFixedDepositAccountsAccountChartCurrency.from_json(json)
# print the JSON string representation of the object
print(GetFixedDepositAccountsAccountChartCurrency.to_json())

# convert the object into a dict
get_fixed_deposit_accounts_account_chart_currency_dict = get_fixed_deposit_accounts_account_chart_currency_instance.to_dict()
# create an instance of GetFixedDepositAccountsAccountChartCurrency from a dict
get_fixed_deposit_accounts_account_chart_currency_from_dict = GetFixedDepositAccountsAccountChartCurrency.from_dict(get_fixed_deposit_accounts_account_chart_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


