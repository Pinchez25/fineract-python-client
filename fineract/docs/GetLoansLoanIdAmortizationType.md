# GetLoansLoanIdAmortizationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_amortization_type import GetLoansLoanIdAmortizationType

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdAmortizationType from a JSON string
get_loans_loan_id_amortization_type_instance = GetLoansLoanIdAmortizationType.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdAmortizationType.to_json()

# convert the object into a dict
get_loans_loan_id_amortization_type_dict = get_loans_loan_id_amortization_type_instance.to_dict()
# create an instance of GetLoansLoanIdAmortizationType from a dict
get_loans_loan_id_amortization_type_form_dict = get_loans_loan_id_amortization_type.from_dict(get_loans_loan_id_amortization_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


