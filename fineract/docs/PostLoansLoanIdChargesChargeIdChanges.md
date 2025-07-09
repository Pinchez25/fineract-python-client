# PostLoansLoanIdChargesChargeIdChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**charge_id** | **int** |  | [optional] 
**var_date** | **float** |  | [optional] 
**due_date** | **date** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fee_charges_portion** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**installment_number** | **int** |  | [optional] 
**interest_portion** | **float** |  | [optional] 
**locale** | **str** |  | [optional] 
**outstanding_loan_balance** | **float** |  | [optional] 
**penalty_charges_portion** | **float** |  | [optional] 
**principal_portion** | **float** |  | [optional] 
**transaction_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_charges_charge_id_changes import PostLoansLoanIdChargesChargeIdChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdChargesChargeIdChanges from a JSON string
post_loans_loan_id_charges_charge_id_changes_instance = PostLoansLoanIdChargesChargeIdChanges.from_json(json)
# print the JSON string representation of the object
print PostLoansLoanIdChargesChargeIdChanges.to_json()

# convert the object into a dict
post_loans_loan_id_charges_charge_id_changes_dict = post_loans_loan_id_charges_charge_id_changes_instance.to_dict()
# create an instance of PostLoansLoanIdChargesChargeIdChanges from a dict
post_loans_loan_id_charges_charge_id_changes_form_dict = post_loans_loan_id_charges_charge_id_changes.from_dict(post_loans_loan_id_charges_charge_id_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


