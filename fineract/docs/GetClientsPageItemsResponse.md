# GetClientsPageItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**fullname** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**status** | [**GetClientStatus**](GetClientStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_page_items_response import GetClientsPageItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsPageItemsResponse from a JSON string
get_clients_page_items_response_instance = GetClientsPageItemsResponse.from_json(json)
# print the JSON string representation of the object
print(GetClientsPageItemsResponse.to_json())

# convert the object into a dict
get_clients_page_items_response_dict = get_clients_page_items_response_instance.to_dict()
# create an instance of GetClientsPageItemsResponse from a dict
get_clients_page_items_response_from_dict = GetClientsPageItemsResponse.from_dict(get_clients_page_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


