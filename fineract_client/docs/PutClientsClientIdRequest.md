# PutClientsClientIdRequest

PutClientsClientIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | [optional] 
**resource_external_id** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_clients_client_id_request import PutClientsClientIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutClientsClientIdRequest from a JSON string
put_clients_client_id_request_instance = PutClientsClientIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutClientsClientIdRequest.to_json())

# convert the object into a dict
put_clients_client_id_request_dict = put_clients_client_id_request_instance.to_dict()
# create an instance of PutClientsClientIdRequest from a dict
put_clients_client_id_request_from_dict = PutClientsClientIdRequest.from_dict(put_clients_client_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


