# PostStaffRequest

PostStaffRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_loan_officer** | **bool** |  | [optional] 
**joining_date** | **date** |  | [optional] 
**lastname** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**mobile_no** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_staff_request import PostStaffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostStaffRequest from a JSON string
post_staff_request_instance = PostStaffRequest.from_json(json)
# print the JSON string representation of the object
print(PostStaffRequest.to_json())

# convert the object into a dict
post_staff_request_dict = post_staff_request_instance.to_dict()
# create an instance of PostStaffRequest from a dict
post_staff_request_from_dict = PostStaffRequest.from_dict(post_staff_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


