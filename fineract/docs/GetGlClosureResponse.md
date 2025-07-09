# GetGlClosureResponse

GetGLClosureResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closing_date** | **date** |  | [optional] 
**comments** | **str** |  | [optional] 
**created_by_user_id** | **int** |  | [optional] 
**created_by_username** | **str** |  | [optional] 
**created_date** | **date** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**last_updated_by_user_id** | **int** |  | [optional] 
**last_updated_by_username** | **str** |  | [optional] 
**last_updated_date** | **date** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_gl_closure_response import GetGlClosureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGlClosureResponse from a JSON string
get_gl_closure_response_instance = GetGlClosureResponse.from_json(json)
# print the JSON string representation of the object
print GetGlClosureResponse.to_json()

# convert the object into a dict
get_gl_closure_response_dict = get_gl_closure_response_instance.to_dict()
# create an instance of GetGlClosureResponse from a dict
get_gl_closure_response_form_dict = get_gl_closure_response.from_dict(get_gl_closure_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


