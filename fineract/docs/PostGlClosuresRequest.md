# PostGlClosuresRequest

PostGLCLosuresRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closing_date** | **date** |  | [optional] 
**comments** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_gl_closures_request import PostGlClosuresRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostGlClosuresRequest from a JSON string
post_gl_closures_request_instance = PostGlClosuresRequest.from_json(json)
# print the JSON string representation of the object
print PostGlClosuresRequest.to_json()

# convert the object into a dict
post_gl_closures_request_dict = post_gl_closures_request_instance.to_dict()
# create an instance of PostGlClosuresRequest from a dict
post_gl_closures_request_form_dict = post_gl_closures_request.from_dict(post_gl_closures_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


