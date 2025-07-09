# PostSelfAuthenticationResponse

PostSelfAuthenticationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticated** | **bool** |  | [optional] 
**base64_encoded_authentication_key** | **str** |  | [optional] 
**clients** | **List[int]** |  | [optional] 
**is_self_service_user** | **bool** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**organisational_role** | [**GetSelfUserDetailsOrganisationalRole**](GetSelfUserDetailsOrganisationalRole.md) |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**roles** | [**List[GetSelfUserDetailsRoles]**](GetSelfUserDetailsRoles.md) |  | [optional] 
**staff_display_name** | **str** |  | [optional] 
**staff_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_self_authentication_response import PostSelfAuthenticationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostSelfAuthenticationResponse from a JSON string
post_self_authentication_response_instance = PostSelfAuthenticationResponse.from_json(json)
# print the JSON string representation of the object
print(PostSelfAuthenticationResponse.to_json())

# convert the object into a dict
post_self_authentication_response_dict = post_self_authentication_response_instance.to_dict()
# create an instance of PostSelfAuthenticationResponse from a dict
post_self_authentication_response_from_dict = PostSelfAuthenticationResponse.from_dict(post_self_authentication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


