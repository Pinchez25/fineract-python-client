# DeleteLoansLoanIdChargesChargeIdResponse

DeleteLoansLoanIdChargesChargeIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_external_id** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_loans_loan_id_charges_charge_id_response import DeleteLoansLoanIdChargesChargeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteLoansLoanIdChargesChargeIdResponse from a JSON string
delete_loans_loan_id_charges_charge_id_response_instance = DeleteLoansLoanIdChargesChargeIdResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteLoansLoanIdChargesChargeIdResponse.to_json())

# convert the object into a dict
delete_loans_loan_id_charges_charge_id_response_dict = delete_loans_loan_id_charges_charge_id_response_instance.to_dict()
# create an instance of DeleteLoansLoanIdChargesChargeIdResponse from a dict
delete_loans_loan_id_charges_charge_id_response_from_dict = DeleteLoansLoanIdChargesChargeIdResponse.from_dict(delete_loans_loan_id_charges_charge_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


