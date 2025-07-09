# GroupRoleData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**role** | [**CodeValueData**](CodeValueData.md) |  | [optional] 

## Example

```python
from fineract_client.models.group_role_data import GroupRoleData

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRoleData from a JSON string
group_role_data_instance = GroupRoleData.from_json(json)
# print the JSON string representation of the object
print GroupRoleData.to_json()

# convert the object into a dict
group_role_data_dict = group_role_data_instance.to_dict()
# create an instance of GroupRoleData from a dict
group_role_data_form_dict = group_role_data.from_dict(group_role_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


