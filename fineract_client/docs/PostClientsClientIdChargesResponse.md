# PostClientsClientIdChargesResponse

PostClientsClientIdChargesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_clients_client_id_charges_response import PostClientsClientIdChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientsClientIdChargesResponse from a JSON string
post_clients_client_id_charges_response_instance = PostClientsClientIdChargesResponse.from_json(json)
# print the JSON string representation of the object
print(PostClientsClientIdChargesResponse.to_json())

# convert the object into a dict
post_clients_client_id_charges_response_dict = post_clients_client_id_charges_response_instance.to_dict()
# create an instance of PostClientsClientIdChargesResponse from a dict
post_clients_client_id_charges_response_from_dict = PostClientsClientIdChargesResponse.from_dict(post_clients_client_id_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


