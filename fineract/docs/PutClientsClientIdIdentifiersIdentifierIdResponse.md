# PutClientsClientIdIdentifiersIdentifierIdResponse

PutClientsClientIdIdentifiersIdentifierIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutClientsClientIdIdentifiersIdentifierIdRequest**](PutClientsClientIdIdentifiersIdentifierIdRequest.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_clients_client_id_identifiers_identifier_id_response import PutClientsClientIdIdentifiersIdentifierIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutClientsClientIdIdentifiersIdentifierIdResponse from a JSON string
put_clients_client_id_identifiers_identifier_id_response_instance = PutClientsClientIdIdentifiersIdentifierIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutClientsClientIdIdentifiersIdentifierIdResponse.to_json())

# convert the object into a dict
put_clients_client_id_identifiers_identifier_id_response_dict = put_clients_client_id_identifiers_identifier_id_response_instance.to_dict()
# create an instance of PutClientsClientIdIdentifiersIdentifierIdResponse from a dict
put_clients_client_id_identifiers_identifier_id_response_from_dict = PutClientsClientIdIdentifiersIdentifierIdResponse.from_dict(put_clients_client_id_identifiers_identifier_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


