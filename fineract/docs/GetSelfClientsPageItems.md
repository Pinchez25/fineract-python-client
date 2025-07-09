# GetSelfClientsPageItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**activation_date** | **date** |  | [optional] 
**active** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**fullname** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**status** | [**GetSelfClientsStatus**](GetSelfClientsStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_page_items import GetSelfClientsPageItems

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsPageItems from a JSON string
get_self_clients_page_items_instance = GetSelfClientsPageItems.from_json(json)
# print the JSON string representation of the object
print(GetSelfClientsPageItems.to_json())

# convert the object into a dict
get_self_clients_page_items_dict = get_self_clients_page_items_instance.to_dict()
# create an instance of GetSelfClientsPageItems from a dict
get_self_clients_page_items_from_dict = GetSelfClientsPageItems.from_dict(get_self_clients_page_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


