# PostCreateRescheduleLoansRequest

PostCreateRescheduleLoansRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_due_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**extra_terms** | **int** |  | [optional] 
**grace_on_interest** | **int** |  | [optional] 
**grace_on_principal** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**new_interest_rate** | **float** |  | [optional] 
**reschedule_from_date** | **str** |  | [optional] 
**reschedule_reason_comment** | **str** |  | [optional] 
**reschedule_reason_id** | **int** |  | [optional] 
**submitted_on_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_create_reschedule_loans_request import PostCreateRescheduleLoansRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateRescheduleLoansRequest from a JSON string
post_create_reschedule_loans_request_instance = PostCreateRescheduleLoansRequest.from_json(json)
# print the JSON string representation of the object
print(PostCreateRescheduleLoansRequest.to_json())

# convert the object into a dict
post_create_reschedule_loans_request_dict = post_create_reschedule_loans_request_instance.to_dict()
# create an instance of PostCreateRescheduleLoansRequest from a dict
post_create_reschedule_loans_request_from_dict = PostCreateRescheduleLoansRequest.from_dict(post_create_reschedule_loans_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


