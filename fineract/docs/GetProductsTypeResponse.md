# GetProductsTypeResponse

GetProductsTypeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetProductsPageItems]**](GetProductsPageItems.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_products_type_response import GetProductsTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsTypeResponse from a JSON string
get_products_type_response_instance = GetProductsTypeResponse.from_json(json)
# print the JSON string representation of the object
print(GetProductsTypeResponse.to_json())

# convert the object into a dict
get_products_type_response_dict = get_products_type_response_instance.to_dict()
# create an instance of GetProductsTypeResponse from a dict
get_products_type_response_from_dict = GetProductsTypeResponse.from_dict(get_products_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


