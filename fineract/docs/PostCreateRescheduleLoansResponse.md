# PostCreateRescheduleLoansResponse

PostCreateRescheduleLoansResponse 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_create_reschedule_loans_response import PostCreateRescheduleLoansResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateRescheduleLoansResponse from a JSON string
post_create_reschedule_loans_response_instance = PostCreateRescheduleLoansResponse.from_json(json)
# print the JSON string representation of the object
print PostCreateRescheduleLoansResponse.to_json()

# convert the object into a dict
post_create_reschedule_loans_response_dict = post_create_reschedule_loans_response_instance.to_dict()
# create an instance of PostCreateRescheduleLoansResponse from a dict
post_create_reschedule_loans_response_form_dict = post_create_reschedule_loans_response.from_dict(post_create_reschedule_loans_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


