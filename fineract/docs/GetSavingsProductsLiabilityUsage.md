# GetSavingsProductsLiabilityUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_products_liability_usage import GetSavingsProductsLiabilityUsage

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsProductsLiabilityUsage from a JSON string
get_savings_products_liability_usage_instance = GetSavingsProductsLiabilityUsage.from_json(json)
# print the JSON string representation of the object
print(GetSavingsProductsLiabilityUsage.to_json())

# convert the object into a dict
get_savings_products_liability_usage_dict = get_savings_products_liability_usage_instance.to_dict()
# create an instance of GetSavingsProductsLiabilityUsage from a dict
get_savings_products_liability_usage_from_dict = GetSavingsProductsLiabilityUsage.from_dict(get_savings_products_liability_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


