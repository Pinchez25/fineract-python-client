# GetLoanProductsResponse

GetLoanProductsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_rule** | [**GetLoanProductsAccountingRule**](GetLoanProductsAccountingRule.md) |  | [optional] 
**amortization_type** | [**GetLoanProductsAmortizationType**](GetLoanProductsAmortizationType.md) |  | [optional] 
**annual_interest_rate** | **float** |  | [optional] 
**currency** | [**GetLoanProductsCurrency**](GetLoanProductsCurrency.md) |  | [optional] 
**days_in_month_type** | [**GetLoansProductsDaysInMonthType**](GetLoansProductsDaysInMonthType.md) |  | [optional] 
**days_in_year_type** | [**GetLoansProductsDaysInYearType**](GetLoansProductsDaysInYearType.md) |  | [optional] 
**end_date** | **date** |  | [optional] 
**fixed_length** | **int** |  | [optional] 
**fixed_principal_percentage_per_installment** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**include_in_borrower_cycle** | **bool** |  | [optional] 
**interest_calculation_period_type** | [**GetLoansProductsInterestCalculationPeriodType**](GetLoansProductsInterestCalculationPeriodType.md) |  | [optional] 
**interest_rate_frequency_type** | [**GetLoanProductsInterestRateFrequencyType**](GetLoanProductsInterestRateFrequencyType.md) |  | [optional] 
**interest_rate_per_period** | **float** |  | [optional] 
**interest_rate_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**interest_recalculation_data** | [**GetLoanProductsInterestRecalculationData**](GetLoanProductsInterestRecalculationData.md) |  | [optional] 
**interest_type** | [**GetLoanProductsInterestType**](GetLoanProductsInterestType.md) |  | [optional] 
**is_interest_recalculation_enabled** | **bool** |  | [optional] 
**max_number_of_repayments** | **int** |  | [optional] 
**max_principal** | **float** |  | [optional] 
**min_number_of_repayments** | **int** |  | [optional] 
**min_principal** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**number_of_repayment_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**principal** | **float** |  | [optional] 
**principal_threshold_for_last_instalment** | **int** |  | [optional] 
**principal_variations_for_borrower_cycle** | **List[int]** |  | [optional] 
**repayment_every** | **int** |  | [optional] 
**repayment_frequency_type** | [**GetLoanProductsRepaymentFrequencyType**](GetLoanProductsRepaymentFrequencyType.md) |  | [optional] 
**repayment_start_date_type** | [**GetLoanProductsRepaymentStartDateType**](GetLoanProductsRepaymentStartDateType.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**status** | **str** |  | [optional] 
**supported_interest_refund_types** | [**List[StringEnumOptionData]**](StringEnumOptionData.md) |  | [optional] 
**transaction_processing_strategy** | **str** |  | [optional] 
**transaction_processing_strategy_name** | **str** |  | [optional] 
**use_borrower_cycle** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_products_response import GetLoanProductsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanProductsResponse from a JSON string
get_loan_products_response_instance = GetLoanProductsResponse.from_json(json)
# print the JSON string representation of the object
print(GetLoanProductsResponse.to_json())

# convert the object into a dict
get_loan_products_response_dict = get_loan_products_response_instance.to_dict()
# create an instance of GetLoanProductsResponse from a dict
get_loan_products_response_from_dict = GetLoanProductsResponse.from_dict(get_loan_products_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


