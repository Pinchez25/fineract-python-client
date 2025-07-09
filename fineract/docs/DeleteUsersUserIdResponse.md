# DeleteUsersUserIdResponse

DeleteUsersUserIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **object** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_users_user_id_response import DeleteUsersUserIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUsersUserIdResponse from a JSON string
delete_users_user_id_response_instance = DeleteUsersUserIdResponse.from_json(json)
# print the JSON string representation of the object
print DeleteUsersUserIdResponse.to_json()

# convert the object into a dict
delete_users_user_id_response_dict = delete_users_user_id_response_instance.to_dict()
# create an instance of DeleteUsersUserIdResponse from a dict
delete_users_user_id_response_form_dict = delete_users_user_id_response.from_dict(delete_users_user_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


