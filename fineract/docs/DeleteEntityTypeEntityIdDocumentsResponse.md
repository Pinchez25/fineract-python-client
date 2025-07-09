# DeleteEntityTypeEntityIdDocumentsResponse

DeleteEntityTypeEntityIdDocumentsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **object** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**resource_identifier** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.delete_entity_type_entity_id_documents_response import DeleteEntityTypeEntityIdDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteEntityTypeEntityIdDocumentsResponse from a JSON string
delete_entity_type_entity_id_documents_response_instance = DeleteEntityTypeEntityIdDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print DeleteEntityTypeEntityIdDocumentsResponse.to_json()

# convert the object into a dict
delete_entity_type_entity_id_documents_response_dict = delete_entity_type_entity_id_documents_response_instance.to_dict()
# create an instance of DeleteEntityTypeEntityIdDocumentsResponse from a dict
delete_entity_type_entity_id_documents_response_form_dict = delete_entity_type_entity_id_documents_response.from_dict(delete_entity_type_entity_id_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


