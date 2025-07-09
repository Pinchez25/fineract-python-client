# PutEntityTypeEntityIdDocumentsResponse

PutEntityTypeEntityIdDocumentsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **object** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**resource_identifier** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_entity_type_entity_id_documents_response import PutEntityTypeEntityIdDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutEntityTypeEntityIdDocumentsResponse from a JSON string
put_entity_type_entity_id_documents_response_instance = PutEntityTypeEntityIdDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print PutEntityTypeEntityIdDocumentsResponse.to_json()

# convert the object into a dict
put_entity_type_entity_id_documents_response_dict = put_entity_type_entity_id_documents_response_instance.to_dict()
# create an instance of PutEntityTypeEntityIdDocumentsResponse from a dict
put_entity_type_entity_id_documents_response_form_dict = put_entity_type_entity_id_documents_response.from_dict(put_entity_type_entity_id_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


