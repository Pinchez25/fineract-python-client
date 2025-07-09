# GetUsersUserIdResponse

GetUsersUserIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_roles** | [**List[RoleData]**](RoleData.md) |  | [optional] 
**email** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**lastname** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**password_never_expires** | **bool** |  | [optional] 
**selected_roles** | [**List[RoleData]**](RoleData.md) |  | [optional] 
**staff** | [**StaffData**](StaffData.md) |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_users_user_id_response import GetUsersUserIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsersUserIdResponse from a JSON string
get_users_user_id_response_instance = GetUsersUserIdResponse.from_json(json)
# print the JSON string representation of the object
print GetUsersUserIdResponse.to_json()

# convert the object into a dict
get_users_user_id_response_dict = get_users_user_id_response_instance.to_dict()
# create an instance of GetUsersUserIdResponse from a dict
get_users_user_id_response_form_dict = get_users_user_id_response.from_dict(get_users_user_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


