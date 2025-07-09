# GetLoansLoanIdResponse

GetLoansLoanIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**amortization_type** | [**GetLoansLoanIdAmortizationType**](GetLoansLoanIdAmortizationType.md) |  | [optional] 
**annual_interest_rate** | **float** |  | [optional] 
**approved_principal** | **float** |  | [optional] 
**charged_off** | **bool** |  | [optional] 
**charges** | [**List[GetLoansLoanIdLoanChargeData]**](GetLoansLoanIdLoanChargeData.md) | Set of charges | [optional] 
**client_external_id** | **str** |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**client_office_id** | **int** |  | [optional] 
**currency** | [**GetLoansLoanIdCurrency**](GetLoansLoanIdCurrency.md) |  | [optional] 
**delinquency_range** | [**GetDelinquencyRangesResponse**](GetDelinquencyRangesResponse.md) |  | [optional] 
**delinquent** | [**GetLoansLoanIdDelinquencySummary**](GetLoansLoanIdDelinquencySummary.md) |  | [optional] 
**disallow_expected_disbursements** | **bool** |  | [optional] 
**disbursed_amount_percentage_for_down_payment** | **float** |  | [optional] 
**disbursement_details** | [**List[GetLoansLoanIdDisbursementDetails]**](GetLoansLoanIdDisbursementDetails.md) | Set of GetLoansLoanIdDisbursementDetails | [optional] 
**enable_auto_repayment_for_down_payment** | **bool** |  | [optional] 
**enable_down_payment** | **bool** |  | [optional] 
**enable_installment_level_delinquency** | **bool** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fixed_length** | **int** |  | [optional] 
**fixed_principal_percentage_per_installment** | **float** |  | [optional] 
**fraud** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**in_arrears_tolerance** | **int** |  | [optional] 
**interest_calculation_period_type** | [**GetLoansLoanIdInterestCalculationPeriodType**](GetLoansLoanIdInterestCalculationPeriodType.md) |  | [optional] 
**interest_rate_frequency_type** | [**GetLoansLoanIdInterestRateFrequencyType**](GetLoansLoanIdInterestRateFrequencyType.md) |  | [optional] 
**interest_rate_per_period** | **float** |  | [optional] 
**interest_type** | [**GetLoansLoanIdInterestType**](GetLoansLoanIdInterestType.md) |  | [optional] 
**is_floating_interest_rate** | **bool** |  | [optional] 
**last_closed_business_date** | **date** |  | [optional] 
**loan_officer_id** | **int** |  | [optional] 
**loan_officer_name** | **str** |  | [optional] 
**loan_product_description** | **str** |  | [optional] 
**loan_product_id** | **int** |  | [optional] 
**loan_product_name** | **str** |  | [optional] 
**loan_purpose_id** | **int** |  | [optional] 
**loan_purpose_name** | **str** |  | [optional] 
**loan_schedule_processing_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**loan_schedule_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**loan_type** | [**GetLoansLoanIdLoanType**](GetLoansLoanIdLoanType.md) |  | [optional] 
**net_disbursal_amount** | **float** |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**overpaid_on_date** | **date** |  | [optional] 
**principal** | **float** |  | [optional] 
**proposed_principal** | **float** |  | [optional] 
**repayment_every** | **int** |  | [optional] 
**repayment_frequency_type** | [**GetLoansLoanIdRepaymentFrequencyType**](GetLoansLoanIdRepaymentFrequencyType.md) |  | [optional] 
**repayment_schedule** | [**GetLoansLoanIdRepaymentSchedule**](GetLoansLoanIdRepaymentSchedule.md) |  | [optional] 
**status** | [**GetLoansLoanIdStatus**](GetLoansLoanIdStatus.md) |  | [optional] 
**summary** | [**GetLoansLoanIdSummary**](GetLoansLoanIdSummary.md) |  | [optional] 
**term_frequency** | **int** |  | [optional] 
**term_period_frequency_type** | [**GetLoansLoanIdTermPeriodFrequencyType**](GetLoansLoanIdTermPeriodFrequencyType.md) |  | [optional] 
**timeline** | [**GetLoansLoanIdTimeline**](GetLoansLoanIdTimeline.md) |  | [optional] 
**total_overpaid** | **float** |  | [optional] 
**transaction_processing_strategy_code** | **str** |  | [optional] 
**transactions** | [**List[GetLoansLoanIdTransactions]**](GetLoansLoanIdTransactions.md) | Set of GetLoansLoanIdTransactions | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_response import GetLoansLoanIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdResponse from a JSON string
get_loans_loan_id_response_instance = GetLoansLoanIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdResponse.to_json())

# convert the object into a dict
get_loans_loan_id_response_dict = get_loans_loan_id_response_instance.to_dict()
# create an instance of GetLoansLoanIdResponse from a dict
get_loans_loan_id_response_from_dict = GetLoansLoanIdResponse.from_dict(get_loans_loan_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


