# DeleteGlClosuresResponse

DeleteGlClosuresResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_gl_closures_response import DeleteGlClosuresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteGlClosuresResponse from a JSON string
delete_gl_closures_response_instance = DeleteGlClosuresResponse.from_json(json)
# print the JSON string representation of the object
print DeleteGlClosuresResponse.to_json()

# convert the object into a dict
delete_gl_closures_response_dict = delete_gl_closures_response_instance.to_dict()
# create an instance of DeleteGlClosuresResponse from a dict
delete_gl_closures_response_form_dict = delete_gl_closures_response.from_dict(delete_gl_closures_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


