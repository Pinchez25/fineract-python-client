# GetFixedDepositProductsProductIdChartSlabs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_interest_rate** | **float** |  | [optional] 
**currency** | [**GetFixedDepositProductsProductIdCurrency**](GetFixedDepositProductsProductIdCurrency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**from_period** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**period_type** | [**GetFixedDepositProductsProductIdPeriodType**](GetFixedDepositProductsProductIdPeriodType.md) |  | [optional] 
**to_period** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_fixed_deposit_products_product_id_chart_slabs import GetFixedDepositProductsProductIdChartSlabs

# TODO update the JSON string below
json = "{}"
# create an instance of GetFixedDepositProductsProductIdChartSlabs from a JSON string
get_fixed_deposit_products_product_id_chart_slabs_instance = GetFixedDepositProductsProductIdChartSlabs.from_json(json)
# print the JSON string representation of the object
print GetFixedDepositProductsProductIdChartSlabs.to_json()

# convert the object into a dict
get_fixed_deposit_products_product_id_chart_slabs_dict = get_fixed_deposit_products_product_id_chart_slabs_instance.to_dict()
# create an instance of GetFixedDepositProductsProductIdChartSlabs from a dict
get_fixed_deposit_products_product_id_chart_slabs_form_dict = get_fixed_deposit_products_product_id_chart_slabs.from_dict(get_fixed_deposit_products_product_id_chart_slabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


