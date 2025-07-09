# PostLoansLoanIdRequest

PostLoansLoanIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_disbursement_date** | **str** |  | [optional] 
**approved_loan_amount** | **float** |  | [optional] 
**approved_on_date** | **str** |  | [optional] 
**assignment_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**disbursement_data** | [**List[PostLoansLoanIdDisbursementData]**](PostLoansLoanIdDisbursementData.md) | List of PostLoansLoanIdDisbursementData | [optional] 
**expected_disbursement_date** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**from_loan_officer_id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**rejected_on_date** | **str** |  | [optional] 
**to_loan_officer_id** | **int** |  | [optional] 
**transaction_amount** | **float** |  | [optional] 
**unassigned_date** | **str** |  | [optional] 
**withdrawn_on_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_request import PostLoansLoanIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdRequest from a JSON string
post_loans_loan_id_request_instance = PostLoansLoanIdRequest.from_json(json)
# print the JSON string representation of the object
print PostLoansLoanIdRequest.to_json()

# convert the object into a dict
post_loans_loan_id_request_dict = post_loans_loan_id_request_instance.to_dict()
# create an instance of PostLoansLoanIdRequest from a dict
post_loans_loan_id_request_form_dict = post_loans_loan_id_request.from_dict(post_loans_loan_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


