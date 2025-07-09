# PutClientsClientIdResponse

PutClientsClientIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutClientsClientIdRequest**](PutClientsClientIdRequest.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_external_id** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_clients_client_id_response import PutClientsClientIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutClientsClientIdResponse from a JSON string
put_clients_client_id_response_instance = PutClientsClientIdResponse.from_json(json)
# print the JSON string representation of the object
print PutClientsClientIdResponse.to_json()

# convert the object into a dict
put_clients_client_id_response_dict = put_clients_client_id_response_instance.to_dict()
# create an instance of PutClientsClientIdResponse from a dict
put_clients_client_id_response_form_dict = put_clients_client_id_response.from_dict(put_clients_client_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


