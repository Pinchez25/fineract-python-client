# PostResourceTypeResourceIdNotesResponse

PostResourceTypeResourceIdNotesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_resource_type_resource_id_notes_response import PostResourceTypeResourceIdNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostResourceTypeResourceIdNotesResponse from a JSON string
post_resource_type_resource_id_notes_response_instance = PostResourceTypeResourceIdNotesResponse.from_json(json)
# print the JSON string representation of the object
print(PostResourceTypeResourceIdNotesResponse.to_json())

# convert the object into a dict
post_resource_type_resource_id_notes_response_dict = post_resource_type_resource_id_notes_response_instance.to_dict()
# create an instance of PostResourceTypeResourceIdNotesResponse from a dict
post_resource_type_resource_id_notes_response_from_dict = PostResourceTypeResourceIdNotesResponse.from_dict(post_resource_type_resource_id_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


