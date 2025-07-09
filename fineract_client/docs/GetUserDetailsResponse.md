# GetUserDetailsResponse

GetUserDetailsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**authenticated** | **bool** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**organisational_role** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**roles** | [**List[RoleData]**](RoleData.md) |  | [optional] 
**staff_display_name** | **str** |  | [optional] 
**staff_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_user_details_response import GetUserDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserDetailsResponse from a JSON string
get_user_details_response_instance = GetUserDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserDetailsResponse.to_json())

# convert the object into a dict
get_user_details_response_dict = get_user_details_response_instance.to_dict()
# create an instance of GetUserDetailsResponse from a dict
get_user_details_response_from_dict = GetUserDetailsResponse.from_dict(get_user_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


