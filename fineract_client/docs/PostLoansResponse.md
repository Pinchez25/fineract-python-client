# PostLoansResponse

PostLoansResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**currency** | [**GetLoansLoanIdCurrency**](GetLoansLoanIdCurrency.md) |  | [optional] 
**loan_id** | **int** |  | [optional] 
**loan_term_in_days** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**periods** | [**List[PostLoansRepaymentSchedulePeriods]**](PostLoansRepaymentSchedulePeriods.md) |  | [optional] 
**resource_external_id** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**total_fee_charges_charged** | **int** |  | [optional] 
**total_interest_charged** | **float** |  | [optional] 
**total_outstanding** | **int** |  | [optional] 
**total_penalty_charges_charged** | **int** |  | [optional] 
**total_principal_disbursed** | **int** |  | [optional] 
**total_principal_expected** | **int** |  | [optional] 
**total_principal_paid** | **int** |  | [optional] 
**total_repayment** | **int** |  | [optional] 
**total_repayment_expected** | **float** |  | [optional] 
**total_waived** | **int** |  | [optional] 
**total_written_off** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_response import PostLoansResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansResponse from a JSON string
post_loans_response_instance = PostLoansResponse.from_json(json)
# print the JSON string representation of the object
print(PostLoansResponse.to_json())

# convert the object into a dict
post_loans_response_dict = post_loans_response_instance.to_dict()
# create an instance of PostLoansResponse from a dict
post_loans_response_from_dict = PostLoansResponse.from_dict(post_loans_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


