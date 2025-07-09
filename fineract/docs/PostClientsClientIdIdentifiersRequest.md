# PostClientsClientIdIdentifiersRequest

PostClientsClientIdIdentifiersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**document_key** | **str** |  | [optional] 
**document_type_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_clients_client_id_identifiers_request import PostClientsClientIdIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientsClientIdIdentifiersRequest from a JSON string
post_clients_client_id_identifiers_request_instance = PostClientsClientIdIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print(PostClientsClientIdIdentifiersRequest.to_json())

# convert the object into a dict
post_clients_client_id_identifiers_request_dict = post_clients_client_id_identifiers_request_instance.to_dict()
# create an instance of PostClientsClientIdIdentifiersRequest from a dict
post_clients_client_id_identifiers_request_from_dict = PostClientsClientIdIdentifiersRequest.from_dict(post_clients_client_id_identifiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


