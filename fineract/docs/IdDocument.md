# IdDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_number** | **str** |  | [optional] 
**id_type** | **str** |  | [optional] 
**issuer_country** | **str** |  | [optional] 
**other_id_description** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.id_document import IdDocument

# TODO update the JSON string below
json = "{}"
# create an instance of IdDocument from a JSON string
id_document_instance = IdDocument.from_json(json)
# print the JSON string representation of the object
print IdDocument.to_json()

# convert the object into a dict
id_document_dict = id_document_instance.to_dict()
# create an instance of IdDocument from a dict
id_document_form_dict = id_document.from_dict(id_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


