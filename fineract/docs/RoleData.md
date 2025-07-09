# RoleData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.role_data import RoleData

# TODO update the JSON string below
json = "{}"
# create an instance of RoleData from a JSON string
role_data_instance = RoleData.from_json(json)
# print the JSON string representation of the object
print RoleData.to_json()

# convert the object into a dict
role_data_dict = role_data_instance.to_dict()
# create an instance of RoleData from a dict
role_data_form_dict = role_data.from_dict(role_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


