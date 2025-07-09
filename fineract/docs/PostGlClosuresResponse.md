# PostGlClosuresResponse

PostGlClosuresResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_gl_closures_response import PostGlClosuresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGlClosuresResponse from a JSON string
post_gl_closures_response_instance = PostGlClosuresResponse.from_json(json)
# print the JSON string representation of the object
print PostGlClosuresResponse.to_json()

# convert the object into a dict
post_gl_closures_response_dict = post_gl_closures_response_instance.to_dict()
# create an instance of PostGlClosuresResponse from a dict
post_gl_closures_response_form_dict = post_gl_closures_response.from_dict(post_gl_closures_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


