# GetProductsTypeProductIdResponse

GetProductsTypeProductIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_mapping_options** | [**GetProductsAccountingMappingOptions**](GetProductsAccountingMappingOptions.md) |  | [optional] 
**accounting_mappings** | [**GetProductsAccountingMappings**](GetProductsAccountingMappings.md) |  | [optional] 
**accounting_rule** | [**GetProductsAccountingRule**](GetProductsAccountingRule.md) |  | [optional] 
**allow_dividend_calculation_for_inactive_clients** | **bool** |  | [optional] 
**charge_options** | [**List[GetProductsCharges]**](GetProductsCharges.md) |  | [optional] 
**charges** | [**List[GetProductsCharges]**](GetProductsCharges.md) |  | [optional] 
**currency** | [**GetProductsCurrency**](GetProductsCurrency.md) |  | [optional] 
**currency_options** | [**List[GetChargesCurrency]**](GetChargesCurrency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**lock_period_type_enum** | [**GetLockPeriodTypeEnum**](GetLockPeriodTypeEnum.md) |  | [optional] 
**lockin_period** | **int** |  | [optional] 
**lockin_period_frequency_type_options** | [**List[GetProductsMinimumActivePeriodFrequencyTypeOptions]**](GetProductsMinimumActivePeriodFrequencyTypeOptions.md) |  | [optional] 
**market_price** | [**List[GetProductsMarketPrice]**](GetProductsMarketPrice.md) |  | [optional] 
**maximum_shares** | **int** |  | [optional] 
**minimum_active_period** | **int** |  | [optional] 
**minimum_active_period_for_dividends_type_enum** | [**GetLockPeriodTypeEnum**](GetLockPeriodTypeEnum.md) |  | [optional] 
**minimum_active_period_frequency_type_options** | [**List[GetProductsMinimumActivePeriodFrequencyTypeOptions]**](GetProductsMinimumActivePeriodFrequencyTypeOptions.md) |  | [optional] 
**minimum_shares** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**nominal_shares** | **int** |  | [optional] 
**share_capital** | **int** |  | [optional] 
**short_name** | **str** |  | [optional] 
**total_shares** | **int** |  | [optional] 
**total_shares_issued** | **int** |  | [optional] 
**unit_price** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_products_type_product_id_response import GetProductsTypeProductIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsTypeProductIdResponse from a JSON string
get_products_type_product_id_response_instance = GetProductsTypeProductIdResponse.from_json(json)
# print the JSON string representation of the object
print GetProductsTypeProductIdResponse.to_json()

# convert the object into a dict
get_products_type_product_id_response_dict = get_products_type_product_id_response_instance.to_dict()
# create an instance of GetProductsTypeProductIdResponse from a dict
get_products_type_product_id_response_form_dict = get_products_type_product_id_response.from_dict(get_products_type_product_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


