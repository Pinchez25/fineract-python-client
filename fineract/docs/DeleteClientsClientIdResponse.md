# DeleteClientsClientIdResponse

DeleteClientsClientIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_external_id** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_clients_client_id_response import DeleteClientsClientIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteClientsClientIdResponse from a JSON string
delete_clients_client_id_response_instance = DeleteClientsClientIdResponse.from_json(json)
# print the JSON string representation of the object
print DeleteClientsClientIdResponse.to_json()

# convert the object into a dict
delete_clients_client_id_response_dict = delete_clients_client_id_response_instance.to_dict()
# create an instance of DeleteClientsClientIdResponse from a dict
delete_clients_client_id_response_form_dict = delete_clients_client_id_response.from_dict(delete_clients_client_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


