# PostSavingsProductsResponse

PostSavingsProductsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_savings_products_response import PostSavingsProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostSavingsProductsResponse from a JSON string
post_savings_products_response_instance = PostSavingsProductsResponse.from_json(json)
# print the JSON string representation of the object
print(PostSavingsProductsResponse.to_json())

# convert the object into a dict
post_savings_products_response_dict = post_savings_products_response_instance.to_dict()
# create an instance of PostSavingsProductsResponse from a dict
post_savings_products_response_from_dict = PostSavingsProductsResponse.from_dict(post_savings_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


