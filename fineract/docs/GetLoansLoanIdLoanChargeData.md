# GetLoansLoanIdLoanChargeData

Set of charges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**amount_or_percentage** | **float** |  | [optional] 
**amount_outstanding** | **float** |  | [optional] 
**amount_paid** | **float** |  | [optional] 
**amount_percentage_applied_to** | **float** |  | [optional] 
**amount_waived** | **float** |  | [optional] 
**amount_written_off** | **float** |  | [optional] 
**charge_calculation_type** | [**GetLoansLoanIdEnumOptionData**](GetLoansLoanIdEnumOptionData.md) |  | [optional] 
**charge_id** | **int** |  | [optional] 
**charge_payable** | **bool** |  | [optional] 
**charge_payment_mode** | [**GetLoansLoanIdEnumOptionData**](GetLoansLoanIdEnumOptionData.md) |  | [optional] 
**charge_time_type** | [**GetLoansLoanIdEnumOptionData**](GetLoansLoanIdEnumOptionData.md) |  | [optional] 
**currency** | [**GetLoansLoanIdCurrency**](GetLoansLoanIdCurrency.md) |  | [optional] 
**due_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**installment_charge_data** | [**List[GetLoansLoanIdLoanInstallmentChargeData]**](GetLoansLoanIdLoanInstallmentChargeData.md) | List of GetLoansLoanIdLoanInstallmentChargeData | [optional] 
**loan_id** | **int** |  | [optional] 
**max_cap** | **float** |  | [optional] 
**min_cap** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**paid** | **bool** |  | [optional] 
**penalty** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 
**waived** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_loan_charge_data import GetLoansLoanIdLoanChargeData

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdLoanChargeData from a JSON string
get_loans_loan_id_loan_charge_data_instance = GetLoansLoanIdLoanChargeData.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdLoanChargeData.to_json()

# convert the object into a dict
get_loans_loan_id_loan_charge_data_dict = get_loans_loan_id_loan_charge_data_instance.to_dict()
# create an instance of GetLoansLoanIdLoanChargeData from a dict
get_loans_loan_id_loan_charge_data_form_dict = get_loans_loan_id_loan_charge_data.from_dict(get_loans_loan_id_loan_charge_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


