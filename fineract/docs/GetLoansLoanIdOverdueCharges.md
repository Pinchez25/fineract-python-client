# GetLoansLoanIdOverdueCharges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**amount** | **float** |  | [optional] 
**charge_applies_to** | [**GetLoanChargeTemplateChargeAppliesTo**](GetLoanChargeTemplateChargeAppliesTo.md) |  | [optional] 
**charge_calculation_type** | [**GetLoansLoanIdChargeCalculationType**](GetLoansLoanIdChargeCalculationType.md) |  | [optional] 
**charge_payment_mode** | [**GetLoansLoanIdChargePaymentMode**](GetLoansLoanIdChargePaymentMode.md) |  | [optional] 
**charge_time_type** | [**GetLoansLoanIdChargeTimeType**](GetLoansLoanIdChargeTimeType.md) |  | [optional] 
**currency** | [**GetLoanCurrency**](GetLoanCurrency.md) |  | [optional] 
**fee_frequency** | [**GetLoansLoanIdFeeFrequency**](GetLoansLoanIdFeeFrequency.md) |  | [optional] 
**fee_interval** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_overdue_charges import GetLoansLoanIdOverdueCharges

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdOverdueCharges from a JSON string
get_loans_loan_id_overdue_charges_instance = GetLoansLoanIdOverdueCharges.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdOverdueCharges.to_json())

# convert the object into a dict
get_loans_loan_id_overdue_charges_dict = get_loans_loan_id_overdue_charges_instance.to_dict()
# create an instance of GetLoansLoanIdOverdueCharges from a dict
get_loans_loan_id_overdue_charges_from_dict = GetLoansLoanIdOverdueCharges.from_dict(get_loans_loan_id_overdue_charges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


