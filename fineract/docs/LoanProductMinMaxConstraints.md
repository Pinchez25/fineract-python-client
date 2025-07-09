# LoanProductMinMaxConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_nominal_interest_rate_per_period** | **float** |  | [optional] 
**max_number_of_repayments** | **int** |  | [optional] 
**max_principal** | **float** |  | [optional] 
**min_nominal_interest_rate_per_period** | **float** |  | [optional] 
**min_number_of_repayments** | **int** |  | [optional] 
**min_principal** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.loan_product_min_max_constraints import LoanProductMinMaxConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProductMinMaxConstraints from a JSON string
loan_product_min_max_constraints_instance = LoanProductMinMaxConstraints.from_json(json)
# print the JSON string representation of the object
print(LoanProductMinMaxConstraints.to_json())

# convert the object into a dict
loan_product_min_max_constraints_dict = loan_product_min_max_constraints_instance.to_dict()
# create an instance of LoanProductMinMaxConstraints from a dict
loan_product_min_max_constraints_from_dict = LoanProductMinMaxConstraints.from_dict(loan_product_min_max_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


