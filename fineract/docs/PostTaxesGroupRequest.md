# PostTaxesGroupRequest

PostTaxesGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tax_components** | [**List[PostTaxesGroupTaxComponents]**](PostTaxesGroupTaxComponents.md) |  | [optional] 

## Example

```python
from fineract_client.models.post_taxes_group_request import PostTaxesGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTaxesGroupRequest from a JSON string
post_taxes_group_request_instance = PostTaxesGroupRequest.from_json(json)
# print the JSON string representation of the object
print PostTaxesGroupRequest.to_json()

# convert the object into a dict
post_taxes_group_request_dict = post_taxes_group_request_instance.to_dict()
# create an instance of PostTaxesGroupRequest from a dict
post_taxes_group_request_form_dict = post_taxes_group_request.from_dict(post_taxes_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


