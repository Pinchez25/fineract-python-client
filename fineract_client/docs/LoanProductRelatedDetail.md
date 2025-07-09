# LoanProductRelatedDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_partial_period_interest_calcualtion** | **bool** |  | [optional] 
**amortization_method** | **str** |  | [optional] 
**annual_nominal_interest_rate** | **float** |  | [optional] 
**currency** | [**MonetaryCurrency**](MonetaryCurrency.md) |  | [optional] 
**days_in_month_type** | **int** |  | [optional] 
**days_in_year_type** | **int** |  | [optional] 
**disbursed_amount_percentage_for_down_payment** | **float** |  | [optional] 
**enable_accrual_activity_posting** | **bool** |  | [optional] 
**enable_auto_repayment_for_down_payment** | **bool** |  | [optional] 
**enable_down_payment** | **bool** |  | [optional] 
**equal_amortization** | **bool** |  | [optional] 
**fixed_length** | **int** |  | [optional] 
**grace_on_arrears_ageing** | **int** |  | [optional] 
**grace_on_interest_charged** | **int** |  | [optional] 
**grace_on_interest_payment** | **int** |  | [optional] 
**grace_on_principal_payment** | **int** |  | [optional] 
**in_arrears_tolerance** | [**Money**](Money.md) |  | [optional] 
**interest_calculation_period_method** | **str** |  | [optional] 
**interest_method** | **str** |  | [optional] 
**interest_period_frequency_type** | **str** |  | [optional] 
**interest_recalculation_enabled** | **bool** |  | [optional] 
**loan_schedule_processing_type** | **str** |  | [optional] 
**loan_schedule_type** | **str** |  | [optional] 
**nominal_interest_rate_per_period** | **float** |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**principal** | [**Money**](Money.md) |  | [optional] 
**recurring_moratorium_on_principal_periods** | **int** |  | [optional] 
**repay_every** | **int** |  | [optional] 
**repayment_period_frequency_type** | **str** |  | [optional] 
**supported_interest_refund_types** | **List[str]** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_related_detail import LoanProductRelatedDetail

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductRelatedDetail from a JSON string
loan_product_related_detail_instance = LoanProductRelatedDetail.from_json(json)
# print the JSON string representation of the object
print(LoanProductRelatedDetail.to_json())

# convert the object into a dict
loan_product_related_detail_dict = loan_product_related_detail_instance.to_dict()
# create an instance of LoanProductRelatedDetail from a dict
loan_product_related_detail_from_dict = LoanProductRelatedDetail.from_dict(loan_product_related_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


