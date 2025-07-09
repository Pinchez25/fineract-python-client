# PostTemplatesResponse

PostTemplatesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_templates_response import PostTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostTemplatesResponse from a JSON string
post_templates_response_instance = PostTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print PostTemplatesResponse.to_json()

# convert the object into a dict
post_templates_response_dict = post_templates_response_instance.to_dict()
# create an instance of PostTemplatesResponse from a dict
post_templates_response_form_dict = post_templates_response.from_dict(post_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


