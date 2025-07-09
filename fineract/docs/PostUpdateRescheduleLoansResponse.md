# PostUpdateRescheduleLoansResponse

PostUpdateRescheduleLoansResponse 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PostUpdateRescheduleLoanChanges**](PostUpdateRescheduleLoanChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_update_reschedule_loans_response import PostUpdateRescheduleLoansResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostUpdateRescheduleLoansResponse from a JSON string
post_update_reschedule_loans_response_instance = PostUpdateRescheduleLoansResponse.from_json(json)
# print the JSON string representation of the object
print PostUpdateRescheduleLoansResponse.to_json()

# convert the object into a dict
post_update_reschedule_loans_response_dict = post_update_reschedule_loans_response_instance.to_dict()
# create an instance of PostUpdateRescheduleLoansResponse from a dict
post_update_reschedule_loans_response_form_dict = post_update_reschedule_loans_response.from_dict(post_update_reschedule_loans_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


