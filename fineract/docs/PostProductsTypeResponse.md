# PostProductsTypeResponse

PostProductsTypeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_products_type_response import PostProductsTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsTypeResponse from a JSON string
post_products_type_response_instance = PostProductsTypeResponse.from_json(json)
# print the JSON string representation of the object
print(PostProductsTypeResponse.to_json())

# convert the object into a dict
post_products_type_response_dict = post_products_type_response_instance.to_dict()
# create an instance of PostProductsTypeResponse from a dict
post_products_type_response_from_dict = PostProductsTypeResponse.from_dict(post_products_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


