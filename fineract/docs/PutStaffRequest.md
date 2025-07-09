# PutStaffRequest

PutStaffRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** |  | [optional] 
**is_loan_officer** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.put_staff_request import PutStaffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutStaffRequest from a JSON string
put_staff_request_instance = PutStaffRequest.from_json(json)
# print the JSON string representation of the object
print PutStaffRequest.to_json()

# convert the object into a dict
put_staff_request_dict = put_staff_request_instance.to_dict()
# create an instance of PutStaffRequest from a dict
put_staff_request_form_dict = put_staff_request.from_dict(put_staff_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


