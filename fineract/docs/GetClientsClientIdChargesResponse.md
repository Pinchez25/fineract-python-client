# GetClientsClientIdChargesResponse

GetClientsClientIdChargesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetClientsChargesPageItems]**](GetClientsChargesPageItems.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_client_id_charges_response import GetClientsClientIdChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsClientIdChargesResponse from a JSON string
get_clients_client_id_charges_response_instance = GetClientsClientIdChargesResponse.from_json(json)
# print the JSON string representation of the object
print(GetClientsClientIdChargesResponse.to_json())

# convert the object into a dict
get_clients_client_id_charges_response_dict = get_clients_client_id_charges_response_instance.to_dict()
# create an instance of GetClientsClientIdChargesResponse from a dict
get_clients_client_id_charges_response_from_dict = GetClientsClientIdChargesResponse.from_dict(get_clients_client_id_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


