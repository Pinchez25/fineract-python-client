# PutUsersUserIdResponseChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firstname** | **str** |  | [optional] 
**password_encoded** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_users_user_id_response_changes import PutUsersUserIdResponseChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutUsersUserIdResponseChanges from a JSON string
put_users_user_id_response_changes_instance = PutUsersUserIdResponseChanges.from_json(json)
# print the JSON string representation of the object
print PutUsersUserIdResponseChanges.to_json()

# convert the object into a dict
put_users_user_id_response_changes_dict = put_users_user_id_response_changes_instance.to_dict()
# create an instance of PutUsersUserIdResponseChanges from a dict
put_users_user_id_response_changes_form_dict = put_users_user_id_response_changes.from_dict(put_users_user_id_response_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


