# PostFixedDepositProductsCharts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_slabs** | [**List[PostFixedDepositProductsChartSlabs]**](PostFixedDepositProductsChartSlabs.md) |  | [optional] 
**date_format** | **str** |  | [optional] 
**from_date** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_fixed_deposit_products_charts import PostFixedDepositProductsCharts

# TODO update the JSON string below
json = "{}"
# create an instance of PostFixedDepositProductsCharts from a JSON string
post_fixed_deposit_products_charts_instance = PostFixedDepositProductsCharts.from_json(json)
# print the JSON string representation of the object
print PostFixedDepositProductsCharts.to_json()

# convert the object into a dict
post_fixed_deposit_products_charts_dict = post_fixed_deposit_products_charts_instance.to_dict()
# create an instance of PostFixedDepositProductsCharts from a dict
post_fixed_deposit_products_charts_form_dict = post_fixed_deposit_products_charts.from_dict(post_fixed_deposit_products_charts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


