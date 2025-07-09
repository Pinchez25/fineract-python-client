# PostLoansLoanIdScheduleResponse

PostLoansLoanIdScheduleResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PostLoanChanges**](PostLoanChanges.md) |  | [optional] 
**loan_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_schedule_response import PostLoansLoanIdScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdScheduleResponse from a JSON string
post_loans_loan_id_schedule_response_instance = PostLoansLoanIdScheduleResponse.from_json(json)
# print the JSON string representation of the object
print PostLoansLoanIdScheduleResponse.to_json()

# convert the object into a dict
post_loans_loan_id_schedule_response_dict = post_loans_loan_id_schedule_response_instance.to_dict()
# create an instance of PostLoansLoanIdScheduleResponse from a dict
post_loans_loan_id_schedule_response_form_dict = post_loans_loan_id_schedule_response.from_dict(post_loans_loan_id_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


