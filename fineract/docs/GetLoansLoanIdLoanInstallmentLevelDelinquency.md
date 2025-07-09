# GetLoansLoanIdLoanInstallmentLevelDelinquency

List of GetLoansLoanIdLoanInstallmentLevelDelinquency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** |  | [optional] 
**delinquent_amount** | **float** |  | [optional] 
**maximum_age_days** | **int** |  | [optional] 
**minimum_age_days** | **int** |  | [optional] 
**range_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_loan_installment_level_delinquency import GetLoansLoanIdLoanInstallmentLevelDelinquency

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdLoanInstallmentLevelDelinquency from a JSON string
get_loans_loan_id_loan_installment_level_delinquency_instance = GetLoansLoanIdLoanInstallmentLevelDelinquency.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdLoanInstallmentLevelDelinquency.to_json())

# convert the object into a dict
get_loans_loan_id_loan_installment_level_delinquency_dict = get_loans_loan_id_loan_installment_level_delinquency_instance.to_dict()
# create an instance of GetLoansLoanIdLoanInstallmentLevelDelinquency from a dict
get_loans_loan_id_loan_installment_level_delinquency_from_dict = GetLoansLoanIdLoanInstallmentLevelDelinquency.from_dict(get_loans_loan_id_loan_installment_level_delinquency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


