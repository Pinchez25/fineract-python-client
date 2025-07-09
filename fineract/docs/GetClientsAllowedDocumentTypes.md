# GetClientsAllowedDocumentTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_allowed_document_types import GetClientsAllowedDocumentTypes

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsAllowedDocumentTypes from a JSON string
get_clients_allowed_document_types_instance = GetClientsAllowedDocumentTypes.from_json(json)
# print the JSON string representation of the object
print GetClientsAllowedDocumentTypes.to_json()

# convert the object into a dict
get_clients_allowed_document_types_dict = get_clients_allowed_document_types_instance.to_dict()
# create an instance of GetClientsAllowedDocumentTypes from a dict
get_clients_allowed_document_types_form_dict = get_clients_allowed_document_types.from_dict(get_clients_allowed_document_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


