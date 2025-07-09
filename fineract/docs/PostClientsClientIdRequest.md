# PostClientsClientIdRequest

PostClientsClientIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_clients_client_id_request import PostClientsClientIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientsClientIdRequest from a JSON string
post_clients_client_id_request_instance = PostClientsClientIdRequest.from_json(json)
# print the JSON string representation of the object
print PostClientsClientIdRequest.to_json()

# convert the object into a dict
post_clients_client_id_request_dict = post_clients_client_id_request_instance.to_dict()
# create an instance of PostClientsClientIdRequest from a dict
post_clients_client_id_request_form_dict = post_clients_client_id_request.from_dict(post_clients_client_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


