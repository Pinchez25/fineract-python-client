# PostClientsAddressRequest

Address requests

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**address_type_id** | **int** |  | [optional] 
**city** | **str** |  | [optional] 
**country_id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**postal_code** | **int** |  | [optional] 
**state_province_id** | **int** |  | [optional] 
**street** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_clients_address_request import PostClientsAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientsAddressRequest from a JSON string
post_clients_address_request_instance = PostClientsAddressRequest.from_json(json)
# print the JSON string representation of the object
print PostClientsAddressRequest.to_json()

# convert the object into a dict
post_clients_address_request_dict = post_clients_address_request_instance.to_dict()
# create an instance of PostClientsAddressRequest from a dict
post_clients_address_request_form_dict = post_clients_address_request.from_dict(post_clients_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


