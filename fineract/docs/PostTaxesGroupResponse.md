# PostTaxesGroupResponse

PostTaxesGroupResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_taxes_group_response import PostTaxesGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostTaxesGroupResponse from a JSON string
post_taxes_group_response_instance = PostTaxesGroupResponse.from_json(json)
# print the JSON string representation of the object
print PostTaxesGroupResponse.to_json()

# convert the object into a dict
post_taxes_group_response_dict = post_taxes_group_response_instance.to_dict()
# create an instance of PostTaxesGroupResponse from a dict
post_taxes_group_response_form_dict = post_taxes_group_response.from_dict(post_taxes_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


