# PostClientsClientIdChargesRequest

PostClientsClientIdChargesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**charge_id** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_clients_client_id_charges_request import PostClientsClientIdChargesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientsClientIdChargesRequest from a JSON string
post_clients_client_id_charges_request_instance = PostClientsClientIdChargesRequest.from_json(json)
# print the JSON string representation of the object
print(PostClientsClientIdChargesRequest.to_json())

# convert the object into a dict
post_clients_client_id_charges_request_dict = post_clients_client_id_charges_request_instance.to_dict()
# create an instance of PostClientsClientIdChargesRequest from a dict
post_clients_client_id_charges_request_from_dict = PostClientsClientIdChargesRequest.from_dict(post_clients_client_id_charges_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


