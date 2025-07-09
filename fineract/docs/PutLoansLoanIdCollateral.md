# PutLoansLoanIdCollateral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_collateral_id** | **int** |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.put_loans_loan_id_collateral import PutLoansLoanIdCollateral

# TODO update the JSON string below
json = "{}"
# create an instance of PutLoansLoanIdCollateral from a JSON string
put_loans_loan_id_collateral_instance = PutLoansLoanIdCollateral.from_json(json)
# print the JSON string representation of the object
print PutLoansLoanIdCollateral.to_json()

# convert the object into a dict
put_loans_loan_id_collateral_dict = put_loans_loan_id_collateral_instance.to_dict()
# create an instance of PutLoansLoanIdCollateral from a dict
put_loans_loan_id_collateral_form_dict = put_loans_loan_id_collateral.from_dict(put_loans_loan_id_collateral_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


