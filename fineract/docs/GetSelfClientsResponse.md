# GetSelfClientsResponse

GetSelfClientsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetSelfClientsPageItems]**](GetSelfClientsPageItems.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_response import GetSelfClientsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsResponse from a JSON string
get_self_clients_response_instance = GetSelfClientsResponse.from_json(json)
# print the JSON string representation of the object
print GetSelfClientsResponse.to_json()

# convert the object into a dict
get_self_clients_response_dict = get_self_clients_response_instance.to_dict()
# create an instance of GetSelfClientsResponse from a dict
get_self_clients_response_form_dict = get_self_clients_response.from_dict(get_self_clients_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


