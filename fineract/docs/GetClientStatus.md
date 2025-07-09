# GetClientStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_client_status import GetClientStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientStatus from a JSON string
get_client_status_instance = GetClientStatus.from_json(json)
# print the JSON string representation of the object
print GetClientStatus.to_json()

# convert the object into a dict
get_client_status_dict = get_client_status_instance.to_dict()
# create an instance of GetClientStatus from a dict
get_client_status_form_dict = get_client_status.from_dict(get_client_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


