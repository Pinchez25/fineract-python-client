# PutClientsClientIdIdentifiersIdentifierIdRequest

PutClientsClientIdIdentifiersIdentifierIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**document_key** | **str** |  | [optional] 
**document_type_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_clients_client_id_identifiers_identifier_id_request import PutClientsClientIdIdentifiersIdentifierIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutClientsClientIdIdentifiersIdentifierIdRequest from a JSON string
put_clients_client_id_identifiers_identifier_id_request_instance = PutClientsClientIdIdentifiersIdentifierIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutClientsClientIdIdentifiersIdentifierIdRequest.to_json())

# convert the object into a dict
put_clients_client_id_identifiers_identifier_id_request_dict = put_clients_client_id_identifiers_identifier_id_request_instance.to_dict()
# create an instance of PutClientsClientIdIdentifiersIdentifierIdRequest from a dict
put_clients_client_id_identifiers_identifier_id_request_from_dict = PutClientsClientIdIdentifiersIdentifierIdRequest.from_dict(put_clients_client_id_identifiers_identifier_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


