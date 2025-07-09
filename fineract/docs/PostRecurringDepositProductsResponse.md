# PostRecurringDepositProductsResponse

PostRecurringDepositProductsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_recurring_deposit_products_response import PostRecurringDepositProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostRecurringDepositProductsResponse from a JSON string
post_recurring_deposit_products_response_instance = PostRecurringDepositProductsResponse.from_json(json)
# print the JSON string representation of the object
print PostRecurringDepositProductsResponse.to_json()

# convert the object into a dict
post_recurring_deposit_products_response_dict = post_recurring_deposit_products_response_instance.to_dict()
# create an instance of PostRecurringDepositProductsResponse from a dict
post_recurring_deposit_products_response_form_dict = post_recurring_deposit_products_response.from_dict(post_recurring_deposit_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


