# PostLoansLoanIdChargesChargeIdRequest

PostLoansLoanIdChargesChargeIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**charge_id** | **int** |  | [optional] 
**check_number** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**installment_number** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**receipt_number** | **str** |  | [optional] 
**routing_code** | **str** |  | [optional] 
**transaction_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_charges_charge_id_request import PostLoansLoanIdChargesChargeIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdChargesChargeIdRequest from a JSON string
post_loans_loan_id_charges_charge_id_request_instance = PostLoansLoanIdChargesChargeIdRequest.from_json(json)
# print the JSON string representation of the object
print PostLoansLoanIdChargesChargeIdRequest.to_json()

# convert the object into a dict
post_loans_loan_id_charges_charge_id_request_dict = post_loans_loan_id_charges_charge_id_request_instance.to_dict()
# create an instance of PostLoansLoanIdChargesChargeIdRequest from a dict
post_loans_loan_id_charges_charge_id_request_form_dict = post_loans_loan_id_charges_charge_id_request.from_dict(post_loans_loan_id_charges_charge_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


