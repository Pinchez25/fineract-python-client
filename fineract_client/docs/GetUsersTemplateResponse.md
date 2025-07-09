# GetUsersTemplateResponse

GetUsersTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_offices** | [**List[OfficeData]**](OfficeData.md) |  | [optional] 
**available_roles** | [**List[RoleData]**](RoleData.md) |  | [optional] 
**self_service_roles** | [**List[RoleData]**](RoleData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_users_template_response import GetUsersTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsersTemplateResponse from a JSON string
get_users_template_response_instance = GetUsersTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetUsersTemplateResponse.to_json())

# convert the object into a dict
get_users_template_response_dict = get_users_template_response_instance.to_dict()
# create an instance of GetUsersTemplateResponse from a dict
get_users_template_response_from_dict = GetUsersTemplateResponse.from_dict(get_users_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


