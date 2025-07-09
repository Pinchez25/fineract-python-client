# PutSelfUserChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_encoded** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_self_user_changes import PutSelfUserChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutSelfUserChanges from a JSON string
put_self_user_changes_instance = PutSelfUserChanges.from_json(json)
# print the JSON string representation of the object
print PutSelfUserChanges.to_json()

# convert the object into a dict
put_self_user_changes_dict = put_self_user_changes_instance.to_dict()
# create an instance of PutSelfUserChanges from a dict
put_self_user_changes_form_dict = put_self_user_changes.from_dict(put_self_user_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


