# GetProductsLiabilityType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_products_liability_type import GetProductsLiabilityType

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsLiabilityType from a JSON string
get_products_liability_type_instance = GetProductsLiabilityType.from_json(json)
# print the JSON string representation of the object
print(GetProductsLiabilityType.to_json())

# convert the object into a dict
get_products_liability_type_dict = get_products_liability_type_instance.to_dict()
# create an instance of GetProductsLiabilityType from a dict
get_products_liability_type_from_dict = GetProductsLiabilityType.from_dict(get_products_liability_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


