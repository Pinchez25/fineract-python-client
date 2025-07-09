# PostPaymentTypesResponse

PostPaymentTypesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_payment_types_response import PostPaymentTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostPaymentTypesResponse from a JSON string
post_payment_types_response_instance = PostPaymentTypesResponse.from_json(json)
# print the JSON string representation of the object
print PostPaymentTypesResponse.to_json()

# convert the object into a dict
post_payment_types_response_dict = post_payment_types_response_instance.to_dict()
# create an instance of PostPaymentTypesResponse from a dict
post_payment_types_response_form_dict = post_payment_types_response.from_dict(post_payment_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


