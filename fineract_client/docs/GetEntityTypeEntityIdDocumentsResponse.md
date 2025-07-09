# GetEntityTypeEntityIdDocumentsResponse

GetEntityTypeEntityIdDocumentsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**location** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_entity_id** | **int** |  | [optional] 
**parent_entity_type** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**storage_type** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_entity_type_entity_id_documents_response import GetEntityTypeEntityIdDocumentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityTypeEntityIdDocumentsResponse from a JSON string
get_entity_type_entity_id_documents_response_instance = GetEntityTypeEntityIdDocumentsResponse.from_json(json)
# print the JSON string representation of the object
print(GetEntityTypeEntityIdDocumentsResponse.to_json())

# convert the object into a dict
get_entity_type_entity_id_documents_response_dict = get_entity_type_entity_id_documents_response_instance.to_dict()
# create an instance of GetEntityTypeEntityIdDocumentsResponse from a dict
get_entity_type_entity_id_documents_response_from_dict = GetEntityTypeEntityIdDocumentsResponse.from_dict(get_entity_type_entity_id_documents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


