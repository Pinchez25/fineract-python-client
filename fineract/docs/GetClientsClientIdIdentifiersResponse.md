# GetClientsClientIdIdentifiersResponse

GetClientsClientIdIdentifiersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**document_key** | **str** |  | [optional] 
**document_type** | [**GetClientsDocumentType**](GetClientsDocumentType.md) |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_client_id_identifiers_response import GetClientsClientIdIdentifiersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsClientIdIdentifiersResponse from a JSON string
get_clients_client_id_identifiers_response_instance = GetClientsClientIdIdentifiersResponse.from_json(json)
# print the JSON string representation of the object
print GetClientsClientIdIdentifiersResponse.to_json()

# convert the object into a dict
get_clients_client_id_identifiers_response_dict = get_clients_client_id_identifiers_response_instance.to_dict()
# create an instance of GetClientsClientIdIdentifiersResponse from a dict
get_clients_client_id_identifiers_response_form_dict = get_clients_client_id_identifiers_response.from_dict(get_clients_client_id_identifiers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


