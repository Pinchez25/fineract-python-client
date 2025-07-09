# PutUsersUserIdRequest

PutUsersUserIdRequest

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
**repeat_password** | **str** |  | [optional] 
**roles** | **List[int]** |  | [optional] 
**send_password_to_email** | **bool** |  | [optional] 
**staff_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_users_user_id_request import PutUsersUserIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutUsersUserIdRequest from a JSON string
put_users_user_id_request_instance = PutUsersUserIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutUsersUserIdRequest.to_json())

# convert the object into a dict
put_users_user_id_request_dict = put_users_user_id_request_instance.to_dict()
# create an instance of PutUsersUserIdRequest from a dict
put_users_user_id_request_from_dict = PutUsersUserIdRequest.from_dict(put_users_user_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


