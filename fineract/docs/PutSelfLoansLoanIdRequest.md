# PutSelfLoansLoanIdRequest

PutSelfLoansLoanIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amortization_type** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**expected_disbursement_date** | **str** |  | [optional] 
**interest_calculation_period_type** | **int** |  | [optional] 
**interest_rate_per_period** | **int** |  | [optional] 
**interest_type** | **int** |  | [optional] 
**loan_term_frequency** | **int** |  | [optional] 
**loan_term_frequency_type** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**principal** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**repayment_every** | **int** |  | [optional] 
**repayment_frequency_type** | **int** |  | [optional] 
**transaction_processing_strategy_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_self_loans_loan_id_request import PutSelfLoansLoanIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutSelfLoansLoanIdRequest from a JSON string
put_self_loans_loan_id_request_instance = PutSelfLoansLoanIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutSelfLoansLoanIdRequest.to_json())

# convert the object into a dict
put_self_loans_loan_id_request_dict = put_self_loans_loan_id_request_instance.to_dict()
# create an instance of PutSelfLoansLoanIdRequest from a dict
put_self_loans_loan_id_request_from_dict = PutSelfLoansLoanIdRequest.from_dict(put_self_loans_loan_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


