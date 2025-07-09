# PostClientClientIdAddressesRequest

PostClientClientIdAddressesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country_id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**postal_code** | **int** |  | [optional] 
**state_province_id** | **int** |  | [optional] 
**street** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_client_client_id_addresses_request import PostClientClientIdAddressesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientClientIdAddressesRequest from a JSON string
post_client_client_id_addresses_request_instance = PostClientClientIdAddressesRequest.from_json(json)
# print the JSON string representation of the object
print(PostClientClientIdAddressesRequest.to_json())

# convert the object into a dict
post_client_client_id_addresses_request_dict = post_client_client_id_addresses_request_instance.to_dict()
# create an instance of PostClientClientIdAddressesRequest from a dict
post_client_client_id_addresses_request_from_dict = PostClientClientIdAddressesRequest.from_dict(post_client_client_id_addresses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


