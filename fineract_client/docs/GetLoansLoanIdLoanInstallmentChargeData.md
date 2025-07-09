# GetLoansLoanIdLoanInstallmentChargeData

List of GetLoansLoanIdLoanInstallmentChargeData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**amount_accrued** | **float** |  | [optional] 
**amount_outstanding** | **float** |  | [optional] 
**amount_unrecognized** | **float** |  | [optional] 
**amount_waived** | **float** |  | [optional] 
**due_date** | **date** |  | [optional] 
**installment_number** | **int** |  | [optional] 
**paid** | **bool** |  | [optional] 
**waived** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_loan_installment_charge_data import GetLoansLoanIdLoanInstallmentChargeData

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdLoanInstallmentChargeData from a JSON string
get_loans_loan_id_loan_installment_charge_data_instance = GetLoansLoanIdLoanInstallmentChargeData.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdLoanInstallmentChargeData.to_json())

# convert the object into a dict
get_loans_loan_id_loan_installment_charge_data_dict = get_loans_loan_id_loan_installment_charge_data_instance.to_dict()
# create an instance of GetLoansLoanIdLoanInstallmentChargeData from a dict
get_loans_loan_id_loan_installment_charge_data_from_dict = GetLoansLoanIdLoanInstallmentChargeData.from_dict(get_loans_loan_id_loan_installment_charge_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


