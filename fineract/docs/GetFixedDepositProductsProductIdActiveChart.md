# GetFixedDepositProductsProductIdActiveChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_slabs** | [**List[GetFixedDepositProductsProductIdChartSlabs]**](GetFixedDepositProductsProductIdChartSlabs.md) |  | [optional] 
**from_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**period_types** | [**List[GetFixedDepositProductsProductIdPeriodType]**](GetFixedDepositProductsProductIdPeriodType.md) |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_products_product_id_active_chart import GetFixedDepositProductsProductIdActiveChart

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositProductsProductIdActiveChart from a JSON string
get_fixed_deposit_products_product_id_active_chart_instance = GetFixedDepositProductsProductIdActiveChart.from_json(json)
# print the JSON string representation of the object
print GetFixedDepositProductsProductIdActiveChart.to_json()

# convert the object into a dict
get_fixed_deposit_products_product_id_active_chart_dict = get_fixed_deposit_products_product_id_active_chart_instance.to_dict()
# create an instance of GetFixedDepositProductsProductIdActiveChart from a dict
get_fixed_deposit_products_product_id_active_chart_form_dict = get_fixed_deposit_products_product_id_active_chart.from_dict(get_fixed_deposit_products_product_id_active_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


