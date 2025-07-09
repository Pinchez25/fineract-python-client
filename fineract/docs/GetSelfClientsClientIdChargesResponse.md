# GetSelfClientsClientIdChargesResponse

GetSelfClientsClientIdChargesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetSelfClientsChargesPageItems]**](GetSelfClientsChargesPageItems.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_client_id_charges_response import GetSelfClientsClientIdChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsClientIdChargesResponse from a JSON string
get_self_clients_client_id_charges_response_instance = GetSelfClientsClientIdChargesResponse.from_json(json)
# print the JSON string representation of the object
print(GetSelfClientsClientIdChargesResponse.to_json())

# convert the object into a dict
get_self_clients_client_id_charges_response_dict = get_self_clients_client_id_charges_response_instance.to_dict()
# create an instance of GetSelfClientsClientIdChargesResponse from a dict
get_self_clients_client_id_charges_response_from_dict = GetSelfClientsClientIdChargesResponse.from_dict(get_self_clients_client_id_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


