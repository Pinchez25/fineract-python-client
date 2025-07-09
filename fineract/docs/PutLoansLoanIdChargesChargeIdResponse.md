# PutLoansLoanIdChargesChargeIdResponse

PutLoansLoanIdChargesChargeIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutLoansLoanIdChargesChargeIdRequest**](PutLoansLoanIdChargesChargeIdRequest.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_external_id** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_loans_loan_id_charges_charge_id_response import PutLoansLoanIdChargesChargeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutLoansLoanIdChargesChargeIdResponse from a JSON string
put_loans_loan_id_charges_charge_id_response_instance = PutLoansLoanIdChargesChargeIdResponse.from_json(json)
# print the JSON string representation of the object
print PutLoansLoanIdChargesChargeIdResponse.to_json()

# convert the object into a dict
put_loans_loan_id_charges_charge_id_response_dict = put_loans_loan_id_charges_charge_id_response_instance.to_dict()
# create an instance of PutLoansLoanIdChargesChargeIdResponse from a dict
put_loans_loan_id_charges_charge_id_response_form_dict = put_loans_loan_id_charges_charge_id_response.from_dict(put_loans_loan_id_charges_charge_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


