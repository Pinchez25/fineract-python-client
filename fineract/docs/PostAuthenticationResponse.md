# PostAuthenticationResponse

PostAuthenticationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticated** | **bool** |  | [optional] 
**base64_encoded_authentication_key** | **str** |  | [optional] 
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
from fineract_client.models.post_authentication_response import PostAuthenticationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthenticationResponse from a JSON string
post_authentication_response_instance = PostAuthenticationResponse.from_json(json)
# print the JSON string representation of the object
print PostAuthenticationResponse.to_json()

# convert the object into a dict
post_authentication_response_dict = post_authentication_response_instance.to_dict()
# create an instance of PostAuthenticationResponse from a dict
post_authentication_response_form_dict = post_authentication_response.from_dict(post_authentication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


