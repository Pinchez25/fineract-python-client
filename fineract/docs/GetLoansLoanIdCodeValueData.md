# GetLoansLoanIdCodeValueData

List of GetLoansLoanIdCodeValueData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**mandatory** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_code_value_data import GetLoansLoanIdCodeValueData

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdCodeValueData from a JSON string
get_loans_loan_id_code_value_data_instance = GetLoansLoanIdCodeValueData.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdCodeValueData.to_json()

# convert the object into a dict
get_loans_loan_id_code_value_data_dict = get_loans_loan_id_code_value_data_instance.to_dict()
# create an instance of GetLoansLoanIdCodeValueData from a dict
get_loans_loan_id_code_value_data_form_dict = get_loans_loan_id_code_value_data.from_dict(get_loans_loan_id_code_value_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


