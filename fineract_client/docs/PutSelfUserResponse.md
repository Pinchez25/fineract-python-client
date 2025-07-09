# PutSelfUserResponse

PutSelfUserResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutSelfUserChanges**](PutSelfUserChanges.md) |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_self_user_response import PutSelfUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutSelfUserResponse from a JSON string
put_self_user_response_instance = PutSelfUserResponse.from_json(json)
# print the JSON string representation of the object
print(PutSelfUserResponse.to_json())

# convert the object into a dict
put_self_user_response_dict = put_self_user_response_instance.to_dict()
# create an instance of PutSelfUserResponse from a dict
put_self_user_response_from_dict = PutSelfUserResponse.from_dict(put_self_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


