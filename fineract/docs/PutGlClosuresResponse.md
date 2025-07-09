# PutGlClosuresResponse

PutGlClosuresResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_gl_closures_response import PutGlClosuresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutGlClosuresResponse from a JSON string
put_gl_closures_response_instance = PutGlClosuresResponse.from_json(json)
# print the JSON string representation of the object
print(PutGlClosuresResponse.to_json())

# convert the object into a dict
put_gl_closures_response_dict = put_gl_closures_response_instance.to_dict()
# create an instance of PutGlClosuresResponse from a dict
put_gl_closures_response_from_dict = PutGlClosuresResponse.from_dict(put_gl_closures_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


