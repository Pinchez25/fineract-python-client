# PostRecurringDepositProductsChartSlabs


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
from fineract_client.models.post_recurring_deposit_products_chart_slabs import PostRecurringDepositProductsChartSlabs

# TODO update the JSON string below
json = "{}"
# create an instance of PostRecurringDepositProductsChartSlabs from a JSON string
post_recurring_deposit_products_chart_slabs_instance = PostRecurringDepositProductsChartSlabs.from_json(json)
# print the JSON string representation of the object
print(PostRecurringDepositProductsChartSlabs.to_json())

# convert the object into a dict
post_recurring_deposit_products_chart_slabs_dict = post_recurring_deposit_products_chart_slabs_instance.to_dict()
# create an instance of PostRecurringDepositProductsChartSlabs from a dict
post_recurring_deposit_products_chart_slabs_from_dict = PostRecurringDepositProductsChartSlabs.from_dict(post_recurring_deposit_products_chart_slabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


