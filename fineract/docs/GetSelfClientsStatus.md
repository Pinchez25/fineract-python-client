# GetSelfClientsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_status import GetSelfClientsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsStatus from a JSON string
get_self_clients_status_instance = GetSelfClientsStatus.from_json(json)
# print the JSON string representation of the object
print(GetSelfClientsStatus.to_json())

# convert the object into a dict
get_self_clients_status_dict = get_self_clients_status_instance.to_dict()
# create an instance of GetSelfClientsStatus from a dict
get_self_clients_status_from_dict = GetSelfClientsStatus.from_dict(get_self_clients_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


