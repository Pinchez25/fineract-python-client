# GetLoansLoanIdLoanType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_loan_type import GetLoansLoanIdLoanType

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdLoanType from a JSON string
get_loans_loan_id_loan_type_instance = GetLoansLoanIdLoanType.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdLoanType.to_json()

# convert the object into a dict
get_loans_loan_id_loan_type_dict = get_loans_loan_id_loan_type_instance.to_dict()
# create an instance of GetLoansLoanIdLoanType from a dict
get_loans_loan_id_loan_type_form_dict = get_loans_loan_id_loan_type.from_dict(get_loans_loan_id_loan_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


