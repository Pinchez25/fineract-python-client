# GetClientsClientIdStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_client_id_status import GetClientsClientIdStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsClientIdStatus from a JSON string
get_clients_client_id_status_instance = GetClientsClientIdStatus.from_json(json)
# print the JSON string representation of the object
print GetClientsClientIdStatus.to_json()

# convert the object into a dict
get_clients_client_id_status_dict = get_clients_client_id_status_instance.to_dict()
# create an instance of GetClientsClientIdStatus from a dict
get_clients_client_id_status_form_dict = get_clients_client_id_status.from_dict(get_clients_client_id_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


