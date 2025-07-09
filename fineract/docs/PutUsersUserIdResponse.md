# PutUsersUserIdResponse

PutUsersUserIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutUsersUserIdResponseChanges**](PutUsersUserIdResponseChanges.md) |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_users_user_id_response import PutUsersUserIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutUsersUserIdResponse from a JSON string
put_users_user_id_response_instance = PutUsersUserIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutUsersUserIdResponse.to_json())

# convert the object into a dict
put_users_user_id_response_dict = put_users_user_id_response_instance.to_dict()
# create an instance of PutUsersUserIdResponse from a dict
put_users_user_id_response_from_dict = PutUsersUserIdResponse.from_dict(put_users_user_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


