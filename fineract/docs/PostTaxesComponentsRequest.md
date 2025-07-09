# PostTaxesComponentsRequest

PostTaxesComponentsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_account_type** | **int** |  | [optional] 
**credit_acount_id** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**percentage** | **float** |  | [optional] 
**start_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_taxes_components_request import PostTaxesComponentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTaxesComponentsRequest from a JSON string
post_taxes_components_request_instance = PostTaxesComponentsRequest.from_json(json)
# print the JSON string representation of the object
print PostTaxesComponentsRequest.to_json()

# convert the object into a dict
post_taxes_components_request_dict = post_taxes_components_request_instance.to_dict()
# create an instance of PostTaxesComponentsRequest from a dict
post_taxes_components_request_form_dict = post_taxes_components_request.from_dict(post_taxes_components_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


