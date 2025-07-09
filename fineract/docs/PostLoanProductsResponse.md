# PostLoanProductsResponse

PostLoanProductsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_loan_products_response import PostLoanProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoanProductsResponse from a JSON string
post_loan_products_response_instance = PostLoanProductsResponse.from_json(json)
# print the JSON string representation of the object
print PostLoanProductsResponse.to_json()

# convert the object into a dict
post_loan_products_response_dict = post_loan_products_response_instance.to_dict()
# create an instance of PostLoanProductsResponse from a dict
post_loan_products_response_form_dict = post_loan_products_response.from_dict(post_loan_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


