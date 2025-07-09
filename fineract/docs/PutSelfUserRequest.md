# PutSelfUserRequest

PutSelfUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**repeat_password** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_self_user_request import PutSelfUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutSelfUserRequest from a JSON string
put_self_user_request_instance = PutSelfUserRequest.from_json(json)
# print the JSON string representation of the object
print PutSelfUserRequest.to_json()

# convert the object into a dict
put_self_user_request_dict = put_self_user_request_instance.to_dict()
# create an instance of PutSelfUserRequest from a dict
put_self_user_request_form_dict = put_self_user_request.from_dict(put_self_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


