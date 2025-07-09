# AppUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_non_expired** | **bool** |  | [optional] 
**account_non_locked** | **bool** |  | [optional] 
**app_user_client_mappings** | [**List[AppUserClientMapping]**](AppUserClientMapping.md) |  | [optional] 
**authorities** | [**List[GrantedAuthority]**](GrantedAuthority.md) |  | [optional] 
**bypass_user** | **bool** |  | [optional] 
**checker_super_user** | **bool** |  | [optional] 
**credentials_non_expired** | **bool** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**firstname** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**last_time_password_updated** | **date** |  | [optional] 
**lastname** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**not_enabled** | **bool** |  | [optional] 
**office** | [**Office**](Office.md) |  | [optional] 
**password** | **str** |  | [optional] 
**password_never_expires** | **bool** |  | [optional] 
**roles** | [**List[Role]**](Role.md) |  | [optional] 
**self_service_user** | **bool** |  | [optional] 
**staff** | [**Staff**](Staff.md) |  | [optional] 
**staff_display_name** | **str** |  | [optional] 
**staff_id** | **int** |  | [optional] 
**system_user** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.app_user import AppUser

# TODO update the JSON string below
json = "{}"
# create an instance of AppUser from a JSON string
app_user_instance = AppUser.from_json(json)
# print the JSON string representation of the object
print AppUser.to_json()

# convert the object into a dict
app_user_dict = app_user_instance.to_dict()
# create an instance of AppUser from a dict
app_user_form_dict = app_user.from_dict(app_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


