# PostPaymentTypesRequest

PostPaymentTypesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_cash_payment** | **bool** |  | [optional] 
**is_system_defined** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_payment_types_request import PostPaymentTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPaymentTypesRequest from a JSON string
post_payment_types_request_instance = PostPaymentTypesRequest.from_json(json)
# print the JSON string representation of the object
print PostPaymentTypesRequest.to_json()

# convert the object into a dict
post_payment_types_request_dict = post_payment_types_request_instance.to_dict()
# create an instance of PostPaymentTypesRequest from a dict
post_payment_types_request_form_dict = post_payment_types_request.from_dict(post_payment_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


