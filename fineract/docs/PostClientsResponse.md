# PostClientsResponse

PostClientsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_external_id** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_clients_response import PostClientsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientsResponse from a JSON string
post_clients_response_instance = PostClientsResponse.from_json(json)
# print the JSON string representation of the object
print PostClientsResponse.to_json()

# convert the object into a dict
post_clients_response_dict = post_clients_response_instance.to_dict()
# create an instance of PostClientsResponse from a dict
post_clients_response_form_dict = post_clients_response.from_dict(post_clients_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


