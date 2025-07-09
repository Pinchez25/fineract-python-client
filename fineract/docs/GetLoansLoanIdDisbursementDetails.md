# GetLoansLoanIdDisbursementDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_disbursement_date** | **date** |  | [optional] 
**approved_principal** | **float** |  | [optional] 
**charge_amount** | **float** |  | [optional] 
**date_format** | **str** |  | [optional] 
**expected_disbursement_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**loan_charge_id** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**net_disbursal_amount** | **float** |  | [optional] 
**note** | **str** |  | [optional] 
**principal** | **float** |  | [optional] 
**waived_charge_amount** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_disbursement_details import GetLoansLoanIdDisbursementDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdDisbursementDetails from a JSON string
get_loans_loan_id_disbursement_details_instance = GetLoansLoanIdDisbursementDetails.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdDisbursementDetails.to_json()

# convert the object into a dict
get_loans_loan_id_disbursement_details_dict = get_loans_loan_id_disbursement_details_instance.to_dict()
# create an instance of GetLoansLoanIdDisbursementDetails from a dict
get_loans_loan_id_disbursement_details_form_dict = get_loans_loan_id_disbursement_details.from_dict(get_loans_loan_id_disbursement_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


