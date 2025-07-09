# CreateStaffResponse

PostStaffResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.create_staff_response import CreateStaffResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStaffResponse from a JSON string
create_staff_response_instance = CreateStaffResponse.from_json(json)
# print the JSON string representation of the object
print CreateStaffResponse.to_json()

# convert the object into a dict
create_staff_response_dict = create_staff_response_instance.to_dict()
# create an instance of CreateStaffResponse from a dict
create_staff_response_form_dict = create_staff_response.from_dict(create_staff_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


