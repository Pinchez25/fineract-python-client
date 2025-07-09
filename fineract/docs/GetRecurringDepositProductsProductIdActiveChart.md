# GetRecurringDepositProductsProductIdActiveChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_slabs** | [**List[GetRecurringDepositProductsProductIdChartSlabs]**](GetRecurringDepositProductsProductIdChartSlabs.md) |  | [optional] 
**from_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**period_types** | [**List[GetRecurringDepositProductsProductIdPeriodType]**](GetRecurringDepositProductsProductIdPeriodType.md) |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_products_product_id_active_chart import GetRecurringDepositProductsProductIdActiveChart

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositProductsProductIdActiveChart from a JSON string
get_recurring_deposit_products_product_id_active_chart_instance = GetRecurringDepositProductsProductIdActiveChart.from_json(json)
# print the JSON string representation of the object
print(GetRecurringDepositProductsProductIdActiveChart.to_json())

# convert the object into a dict
get_recurring_deposit_products_product_id_active_chart_dict = get_recurring_deposit_products_product_id_active_chart_instance.to_dict()
# create an instance of GetRecurringDepositProductsProductIdActiveChart from a dict
get_recurring_deposit_products_product_id_active_chart_from_dict = GetRecurringDepositProductsProductIdActiveChart.from_dict(get_recurring_deposit_products_product_id_active_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


