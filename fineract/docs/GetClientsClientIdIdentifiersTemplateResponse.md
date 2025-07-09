# GetClientsClientIdIdentifiersTemplateResponse

GetClientsClientIdIdentifiersTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_document_types** | [**List[GetClientsAllowedDocumentTypes]**](GetClientsAllowedDocumentTypes.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_client_id_identifiers_template_response import GetClientsClientIdIdentifiersTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsClientIdIdentifiersTemplateResponse from a JSON string
get_clients_client_id_identifiers_template_response_instance = GetClientsClientIdIdentifiersTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetClientsClientIdIdentifiersTemplateResponse.to_json()

# convert the object into a dict
get_clients_client_id_identifiers_template_response_dict = get_clients_client_id_identifiers_template_response_instance.to_dict()
# create an instance of GetClientsClientIdIdentifiersTemplateResponse from a dict
get_clients_client_id_identifiers_template_response_form_dict = get_clients_client_id_identifiers_template_response.from_dict(get_clients_client_id_identifiers_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


