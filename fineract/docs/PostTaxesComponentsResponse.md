# PostTaxesComponentsResponse

PostTaxesComponentsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_taxes_components_response import PostTaxesComponentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostTaxesComponentsResponse from a JSON string
post_taxes_components_response_instance = PostTaxesComponentsResponse.from_json(json)
# print the JSON string representation of the object
print PostTaxesComponentsResponse.to_json()

# convert the object into a dict
post_taxes_components_response_dict = post_taxes_components_response_instance.to_dict()
# create an instance of PostTaxesComponentsResponse from a dict
post_taxes_components_response_form_dict = post_taxes_components_response.from_dict(post_taxes_components_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


