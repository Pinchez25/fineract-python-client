# GetClientsDocumentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_document_type import GetClientsDocumentType

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsDocumentType from a JSON string
get_clients_document_type_instance = GetClientsDocumentType.from_json(json)
# print the JSON string representation of the object
print GetClientsDocumentType.to_json()

# convert the object into a dict
get_clients_document_type_dict = get_clients_document_type_instance.to_dict()
# create an instance of GetClientsDocumentType from a dict
get_clients_document_type_form_dict = get_clients_document_type.from_dict(get_clients_document_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


