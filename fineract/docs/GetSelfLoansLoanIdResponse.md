# GetSelfLoansLoanIdResponse

GetSelfLoansLoanIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**amortization_type** | [**GetLoansLoanIdAmortizationType**](GetLoansLoanIdAmortizationType.md) |  | [optional] 
**annual_interest_rate** | **int** |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**client_office_id** | **int** |  | [optional] 
**currency** | [**GetLoansLoanIdCurrency**](GetLoansLoanIdCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_period_type** | [**GetLoansLoanIdInterestCalculationPeriodType**](GetLoansLoanIdInterestCalculationPeriodType.md) |  | [optional] 
**interest_rate_frequency_type** | [**GetLoansLoanIdInterestRateFrequencyType**](GetLoansLoanIdInterestRateFrequencyType.md) |  | [optional] 
**interest_rate_per_period** | **int** |  | [optional] 
**interest_type** | [**GetLoansLoanIdInterestType**](GetLoansLoanIdInterestType.md) |  | [optional] 
**loan_officer_id** | **int** |  | [optional] 
**loan_officer_name** | **str** |  | [optional] 
**loan_product_description** | **str** |  | [optional] 
**loan_product_id** | **int** |  | [optional] 
**loan_product_name** | **str** |  | [optional] 
**loan_purpose_id** | **int** |  | [optional] 
**loan_purpose_name** | **str** |  | [optional] 
**loan_type** | [**GetLoansLoanIdLoanType**](GetLoansLoanIdLoanType.md) |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**principal** | **int** |  | [optional] 
**repayment_every** | **int** |  | [optional] 
**repayment_frequency_type** | [**GetLoansLoanIdRepaymentFrequencyType**](GetLoansLoanIdRepaymentFrequencyType.md) |  | [optional] 
**status** | [**GetLoansLoanIdStatus**](GetLoansLoanIdStatus.md) |  | [optional] 
**summary** | [**GetSelfLoanIdSummary**](GetSelfLoanIdSummary.md) |  | [optional] 
**term_frequency** | **int** |  | [optional] 
**term_period_frequency_type** | [**GetLoansLoanIdTermPeriodFrequencyType**](GetLoansLoanIdTermPeriodFrequencyType.md) |  | [optional] 
**timeline** | [**GetSelfLoanIdTimeline**](GetSelfLoanIdTimeline.md) |  | [optional] 
**transaction_processing_strategy_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_loans_loan_id_response import GetSelfLoansLoanIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfLoansLoanIdResponse from a JSON string
get_self_loans_loan_id_response_instance = GetSelfLoansLoanIdResponse.from_json(json)
# print the JSON string representation of the object
print GetSelfLoansLoanIdResponse.to_json()

# convert the object into a dict
get_self_loans_loan_id_response_dict = get_self_loans_loan_id_response_instance.to_dict()
# create an instance of GetSelfLoansLoanIdResponse from a dict
get_self_loans_loan_id_response_form_dict = get_self_loans_loan_id_response.from_dict(get_self_loans_loan_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


