# GetClientIdProductIdProductOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_mapping_options** | **object** |  | [optional] 
**accounting_mappings** | [**GetClientIdProductIdAccountingMappings**](GetClientIdProductIdAccountingMappings.md) |  | [optional] 
**accounting_rule** | [**GetShareAccountsClientIdProductIdAccountingRule**](GetShareAccountsClientIdProductIdAccountingRule.md) |  | [optional] 
**allow_dividend_calculation_for_inactive_clients** | **bool** |  | [optional] 
**charge_options** | [**GetShareAccountsChargeOptions**](GetShareAccountsChargeOptions.md) |  | [optional] 
**charges** | **str** |  | [optional] 
**currency** | [**GetShareAccountsCurrency**](GetShareAccountsCurrency.md) |  | [optional] 
**currency_options** | [**GetShareAccountsCurrency**](GetShareAccountsCurrency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**lockin_period** | **int** |  | [optional] 
**lockin_period_enum** | [**GetShareAccountsClientIdProductIdLockPeriodTypeEnum**](GetShareAccountsClientIdProductIdLockPeriodTypeEnum.md) |  | [optional] 
**lockin_period_frequency_type_options** | [**GetClientIdProductIdLockinPeriodFrequencyTypeOptions**](GetClientIdProductIdLockinPeriodFrequencyTypeOptions.md) |  | [optional] 
**market_price** | **str** |  | [optional] 
**maximum_shares** | **int** |  | [optional] 
**minimum_active_period** | **int** |  | [optional] 
**minimum_active_period_for_dividends_type_enum** | [**GetShareAccountsClientIdProductIdMinimumActivePeriodForDividendsTypeEnum**](GetShareAccountsClientIdProductIdMinimumActivePeriodForDividendsTypeEnum.md) |  | [optional] 
**minimum_active_period_frequency_type_options** | [**GetClientIdProductIdMinimumActivePeriodFrequencyTypeOptions**](GetClientIdProductIdMinimumActivePeriodFrequencyTypeOptions.md) |  | [optional] 
**minimum_shares** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**norminal_shares** | **int** |  | [optional] 
**share_capital** | **int** |  | [optional] 
**short_name** | **str** |  | [optional] 
**total_shares** | **int** |  | [optional] 
**total_shares_issued** | **int** |  | [optional] 
**unit_price** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_client_id_product_id_product_options import GetClientIdProductIdProductOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientIdProductIdProductOptions from a JSON string
get_client_id_product_id_product_options_instance = GetClientIdProductIdProductOptions.from_json(json)
# print the JSON string representation of the object
print(GetClientIdProductIdProductOptions.to_json())

# convert the object into a dict
get_client_id_product_id_product_options_dict = get_client_id_product_id_product_options_instance.to_dict()
# create an instance of GetClientIdProductIdProductOptions from a dict
get_client_id_product_id_product_options_from_dict = GetClientIdProductIdProductOptions.from_dict(get_client_id_product_id_product_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


