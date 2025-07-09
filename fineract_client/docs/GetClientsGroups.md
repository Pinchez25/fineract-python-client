# GetClientsGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**external_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_groups import GetClientsGroups

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsGroups from a JSON string
get_clients_groups_instance = GetClientsGroups.from_json(json)
# print the JSON string representation of the object
print(GetClientsGroups.to_json())

# convert the object into a dict
get_clients_groups_dict = get_clients_groups_instance.to_dict()
# create an instance of GetClientsGroups from a dict
get_clients_groups_from_dict = GetClientsGroups.from_dict(get_clients_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


