# PutLoansLoanIdCollateralsCollateralIdResponse

PutLoansLoanIdCollateralsCollateralIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutLoansLoandIdCollateralsCollateralIdRequest**](PutLoansLoandIdCollateralsCollateralIdRequest.md) |  | [optional] 
**loan_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_loans_loan_id_collaterals_collateral_id_response import PutLoansLoanIdCollateralsCollateralIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutLoansLoanIdCollateralsCollateralIdResponse from a JSON string
put_loans_loan_id_collaterals_collateral_id_response_instance = PutLoansLoanIdCollateralsCollateralIdResponse.from_json(json)
# print the JSON string representation of the object
print PutLoansLoanIdCollateralsCollateralIdResponse.to_json()

# convert the object into a dict
put_loans_loan_id_collaterals_collateral_id_response_dict = put_loans_loan_id_collaterals_collateral_id_response_instance.to_dict()
# create an instance of PutLoansLoanIdCollateralsCollateralIdResponse from a dict
put_loans_loan_id_collaterals_collateral_id_response_form_dict = put_loans_loan_id_collaterals_collateral_id_response.from_dict(put_loans_loan_id_collaterals_collateral_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


