# AppUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | [**List[ClientData]**](ClientData.md) |  | [optional] 
**row_index** | **int** |  | [optional] 
**self_service_user** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.app_user_data import AppUserData

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserData from a JSON string
app_user_data_instance = AppUserData.from_json(json)
# print the JSON string representation of the object
print(AppUserData.to_json())

# convert the object into a dict
app_user_data_dict = app_user_data_instance.to_dict()
# create an instance of AppUserData from a dict
app_user_data_from_dict = AppUserData.from_dict(app_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


