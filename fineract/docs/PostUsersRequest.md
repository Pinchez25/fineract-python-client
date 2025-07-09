# PostUsersRequest

PostUsersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | **List[int]** |  | [optional] 
**email** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**is_self_service_user** | **bool** |  | [optional] 
**lastname** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**password** | **str** |  | [optional] 
**password_never_expires** | **bool** |  | [optional] 
**repeat_password** | **str** |  | [optional] 
**roles** | **List[int]** |  | [optional] 
**send_password_to_email** | **bool** |  | [optional] 
**staff_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_users_request import PostUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUsersRequest from a JSON string
post_users_request_instance = PostUsersRequest.from_json(json)
# print the JSON string representation of the object
print PostUsersRequest.to_json()

# convert the object into a dict
post_users_request_dict = post_users_request_instance.to_dict()
# create an instance of PostUsersRequest from a dict
post_users_request_form_dict = post_users_request.from_dict(post_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


