# DeleteClientsClientIdChargesChargeIdResponse

DeleteClientsClientIdChargesChargeIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_clients_client_id_charges_charge_id_response import DeleteClientsClientIdChargesChargeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteClientsClientIdChargesChargeIdResponse from a JSON string
delete_clients_client_id_charges_charge_id_response_instance = DeleteClientsClientIdChargesChargeIdResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteClientsClientIdChargesChargeIdResponse.to_json())

# convert the object into a dict
delete_clients_client_id_charges_charge_id_response_dict = delete_clients_client_id_charges_charge_id_response_instance.to_dict()
# create an instance of DeleteClientsClientIdChargesChargeIdResponse from a dict
delete_clients_client_id_charges_charge_id_response_from_dict = DeleteClientsClientIdChargesChargeIdResponse.from_dict(delete_clients_client_id_charges_charge_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


