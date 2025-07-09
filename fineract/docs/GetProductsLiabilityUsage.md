# GetProductsLiabilityUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_products_liability_usage import GetProductsLiabilityUsage

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsLiabilityUsage from a JSON string
get_products_liability_usage_instance = GetProductsLiabilityUsage.from_json(json)
# print the JSON string representation of the object
print GetProductsLiabilityUsage.to_json()

# convert the object into a dict
get_products_liability_usage_dict = get_products_liability_usage_instance.to_dict()
# create an instance of GetProductsLiabilityUsage from a dict
get_products_liability_usage_form_dict = get_products_liability_usage.from_dict(get_products_liability_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


