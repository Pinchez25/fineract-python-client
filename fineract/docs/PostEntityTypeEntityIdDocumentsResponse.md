# PostEntityTypeEntityIdDocumentsResponse

PostEntityTypeEntityIdDocumentsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 
**resource_identifier** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_entity_type_entity_id_documents_response import PostEntityTypeEntityIdDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostEntityTypeEntityIdDocumentsResponse from a JSON string
post_entity_type_entity_id_documents_response_instance = PostEntityTypeEntityIdDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print PostEntityTypeEntityIdDocumentsResponse.to_json()

# convert the object into a dict
post_entity_type_entity_id_documents_response_dict = post_entity_type_entity_id_documents_response_instance.to_dict()
# create an instance of PostEntityTypeEntityIdDocumentsResponse from a dict
post_entity_type_entity_id_documents_response_form_dict = post_entity_type_entity_id_documents_response.from_dict(post_entity_type_entity_id_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


