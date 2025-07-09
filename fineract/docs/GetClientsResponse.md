# GetClientsResponse

GetClientsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetClientsPageItemsResponse]**](GetClientsPageItemsResponse.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_response import GetClientsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsResponse from a JSON string
get_clients_response_instance = GetClientsResponse.from_json(json)
# print the JSON string representation of the object
print(GetClientsResponse.to_json())

# convert the object into a dict
get_clients_response_dict = get_clients_response_instance.to_dict()
# create an instance of GetClientsResponse from a dict
get_clients_response_from_dict = GetClientsResponse.from_dict(get_clients_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


