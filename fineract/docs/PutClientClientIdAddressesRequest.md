# PutClientClientIdAddressesRequest

PutClientClientIdAddressesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **int** |  | [optional] 
**street** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_client_client_id_addresses_request import PutClientClientIdAddressesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutClientClientIdAddressesRequest from a JSON string
put_client_client_id_addresses_request_instance = PutClientClientIdAddressesRequest.from_json(json)
# print the JSON string representation of the object
print(PutClientClientIdAddressesRequest.to_json())

# convert the object into a dict
put_client_client_id_addresses_request_dict = put_client_client_id_addresses_request_instance.to_dict()
# create an instance of PutClientClientIdAddressesRequest from a dict
put_client_client_id_addresses_request_from_dict = PutClientClientIdAddressesRequest.from_dict(put_client_client_id_addresses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


