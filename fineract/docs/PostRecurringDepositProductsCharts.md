# PostRecurringDepositProductsCharts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_slabs** | [**List[PostRecurringDepositProductsChartSlabs]**](PostRecurringDepositProductsChartSlabs.md) |  | [optional] 
**date_format** | **str** |  | [optional] 
**from_date** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_recurring_deposit_products_charts import PostRecurringDepositProductsCharts

# TODO update the JSON string below
json = "{}"
# create an instance of PostRecurringDepositProductsCharts from a JSON string
post_recurring_deposit_products_charts_instance = PostRecurringDepositProductsCharts.from_json(json)
# print the JSON string representation of the object
print(PostRecurringDepositProductsCharts.to_json())

# convert the object into a dict
post_recurring_deposit_products_charts_dict = post_recurring_deposit_products_charts_instance.to_dict()
# create an instance of PostRecurringDepositProductsCharts from a dict
post_recurring_deposit_products_charts_from_dict = PostRecurringDepositProductsCharts.from_dict(post_recurring_deposit_products_charts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


