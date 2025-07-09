# PutLoansLoanIdDisbursementData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**expected_disbursement_date** | **str** |  | [optional] 
**interest_type** | **int** |  | [optional] 
**is_equal_amortization** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**net_disbursal_amount** | **float** |  | [optional] 
**principal** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.put_loans_loan_id_disbursement_data import PutLoansLoanIdDisbursementData

# TODO update the JSON string below
json = "{}"
# create an instance of PutLoansLoanIdDisbursementData from a JSON string
put_loans_loan_id_disbursement_data_instance = PutLoansLoanIdDisbursementData.from_json(json)
# print the JSON string representation of the object
print(PutLoansLoanIdDisbursementData.to_json())

# convert the object into a dict
put_loans_loan_id_disbursement_data_dict = put_loans_loan_id_disbursement_data_instance.to_dict()
# create an instance of PutLoansLoanIdDisbursementData from a dict
put_loans_loan_id_disbursement_data_from_dict = PutLoansLoanIdDisbursementData.from_dict(put_loans_loan_id_disbursement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


