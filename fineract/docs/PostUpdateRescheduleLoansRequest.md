# PostUpdateRescheduleLoansRequest

PostUpdateRescheduleLoansRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_on_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**rejected_on_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_update_reschedule_loans_request import PostUpdateRescheduleLoansRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostUpdateRescheduleLoansRequest from a JSON string
post_update_reschedule_loans_request_instance = PostUpdateRescheduleLoansRequest.from_json(json)
# print the JSON string representation of the object
print PostUpdateRescheduleLoansRequest.to_json()

# convert the object into a dict
post_update_reschedule_loans_request_dict = post_update_reschedule_loans_request_instance.to_dict()
# create an instance of PostUpdateRescheduleLoansRequest from a dict
post_update_reschedule_loans_request_form_dict = post_update_reschedule_loans_request.from_dict(post_update_reschedule_loans_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


