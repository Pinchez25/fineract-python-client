# UpdateStaffResponse

PutStaffResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.update_staff_response import UpdateStaffResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStaffResponse from a JSON string
update_staff_response_instance = UpdateStaffResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateStaffResponse.to_json())

# convert the object into a dict
update_staff_response_dict = update_staff_response_instance.to_dict()
# create an instance of UpdateStaffResponse from a dict
update_staff_response_from_dict = UpdateStaffResponse.from_dict(update_staff_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


