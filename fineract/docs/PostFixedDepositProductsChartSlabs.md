# PostFixedDepositProductsChartSlabs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_interest_rate** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**from_period** | **int** |  | [optional] 
**period_type** | **int** |  | [optional] 
**to_period** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_fixed_deposit_products_chart_slabs import PostFixedDepositProductsChartSlabs

# TODO update the JSON string below
json = "{}"
# create an instance of PostFixedDepositProductsChartSlabs from a JSON string
post_fixed_deposit_products_chart_slabs_instance = PostFixedDepositProductsChartSlabs.from_json(json)
# print the JSON string representation of the object
print(PostFixedDepositProductsChartSlabs.to_json())

# convert the object into a dict
post_fixed_deposit_products_chart_slabs_dict = post_fixed_deposit_products_chart_slabs_instance.to_dict()
# create an instance of PostFixedDepositProductsChartSlabs from a dict
post_fixed_deposit_products_chart_slabs_from_dict = PostFixedDepositProductsChartSlabs.from_dict(post_fixed_deposit_products_chart_slabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


