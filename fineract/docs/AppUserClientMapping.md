# AppUserClientMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_user** | [**AppUser**](AppUser.md) |  | [optional] 
**client** | [**Client**](Client.md) |  | [optional] 
**id** | **int** |  | [optional] 
**new** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.app_user_client_mapping import AppUserClientMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserClientMapping from a JSON string
app_user_client_mapping_instance = AppUserClientMapping.from_json(json)
# print the JSON string representation of the object
print(AppUserClientMapping.to_json())

# convert the object into a dict
app_user_client_mapping_dict = app_user_client_mapping_instance.to_dict()
# create an instance of AppUserClientMapping from a dict
app_user_client_mapping_from_dict = AppUserClientMapping.from_dict(app_user_client_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


