# PostLoansLoanIdStatus

PostLoansLoanIdStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**closed_obligations_met** | **bool** |  | [optional] 
**closed_rescheduled** | **bool** |  | [optional] 
**closed_written_off** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**overpaid** | **bool** |  | [optional] 
**pending_approval** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**waiting_for_disbursal** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_status import PostLoansLoanIdStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdStatus from a JSON string
post_loans_loan_id_status_instance = PostLoansLoanIdStatus.from_json(json)
# print the JSON string representation of the object
print PostLoansLoanIdStatus.to_json()

# convert the object into a dict
post_loans_loan_id_status_dict = post_loans_loan_id_status_instance.to_dict()
# create an instance of PostLoansLoanIdStatus from a dict
post_loans_loan_id_status_form_dict = post_loans_loan_id_status.from_dict(post_loans_loan_id_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


