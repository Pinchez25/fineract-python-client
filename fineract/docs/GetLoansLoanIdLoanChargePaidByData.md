# GetLoansLoanIdLoanChargePaidByData

List of GetLoansLoanIdLoanChargePaidByData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**charge_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**installment_number** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**transaction_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_loan_charge_paid_by_data import GetLoansLoanIdLoanChargePaidByData

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdLoanChargePaidByData from a JSON string
get_loans_loan_id_loan_charge_paid_by_data_instance = GetLoansLoanIdLoanChargePaidByData.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdLoanChargePaidByData.to_json())

# convert the object into a dict
get_loans_loan_id_loan_charge_paid_by_data_dict = get_loans_loan_id_loan_charge_paid_by_data_instance.to_dict()
# create an instance of GetLoansLoanIdLoanChargePaidByData from a dict
get_loans_loan_id_loan_charge_paid_by_data_from_dict = GetLoansLoanIdLoanChargePaidByData.from_dict(get_loans_loan_id_loan_charge_paid_by_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


