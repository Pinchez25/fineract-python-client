# GetRecurringDepositProductsProductIdChartSlabs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_interest_rate** | **float** |  | [optional] 
**currency** | [**GetRecurringDepositProductsProductIdCurrency**](GetRecurringDepositProductsProductIdCurrency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**from_period** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**period_type** | [**GetRecurringDepositProductsProductIdPeriodType**](GetRecurringDepositProductsProductIdPeriodType.md) |  | [optional] 
**to_period** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_products_product_id_chart_slabs import GetRecurringDepositProductsProductIdChartSlabs

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositProductsProductIdChartSlabs from a JSON string
get_recurring_deposit_products_product_id_chart_slabs_instance = GetRecurringDepositProductsProductIdChartSlabs.from_json(json)
# print the JSON string representation of the object
print(GetRecurringDepositProductsProductIdChartSlabs.to_json())

# convert the object into a dict
get_recurring_deposit_products_product_id_chart_slabs_dict = get_recurring_deposit_products_product_id_chart_slabs_instance.to_dict()
# create an instance of GetRecurringDepositProductsProductIdChartSlabs from a dict
get_recurring_deposit_products_product_id_chart_slabs_from_dict = GetRecurringDepositProductsProductIdChartSlabs.from_dict(get_recurring_deposit_products_product_id_chart_slabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


