# GetClientClientIdAddressesResponse

GetClientClientIdAddressesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **int** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**address_type** | **str** |  | [optional] 
**address_type_id** | **int** |  | [optional] 
**city** | **str** |  | [optional] 
**client_id** | **int** |  | [optional] 
**country_id** | **int** |  | [optional] 
**country_name** | **str** |  | [optional] 
**county_district** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**postal_code** | **int** |  | [optional] 
**state_name** | **str** |  | [optional] 
**state_province_id** | **int** |  | [optional] 
**street** | **str** |  | [optional] 
**town_village** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_client_client_id_addresses_response import GetClientClientIdAddressesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientClientIdAddressesResponse from a JSON string
get_client_client_id_addresses_response_instance = GetClientClientIdAddressesResponse.from_json(json)
# print the JSON string representation of the object
print(GetClientClientIdAddressesResponse.to_json())

# convert the object into a dict
get_client_client_id_addresses_response_dict = get_client_client_id_addresses_response_instance.to_dict()
# create an instance of GetClientClientIdAddressesResponse from a dict
get_client_client_id_addresses_response_from_dict = GetClientClientIdAddressesResponse.from_dict(get_client_client_id_addresses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


