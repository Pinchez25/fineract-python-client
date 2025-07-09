# PutPermissionsRequest

PutPermissionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **Dict[str, bool]** |  | [optional] 

## Example

```python
from fineract_client.models.put_permissions_request import PutPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutPermissionsRequest from a JSON string
put_permissions_request_instance = PutPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print PutPermissionsRequest.to_json()

# convert the object into a dict
put_permissions_request_dict = put_permissions_request_instance.to_dict()
# create an instance of PutPermissionsRequest from a dict
put_permissions_request_form_dict = put_permissions_request.from_dict(put_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


