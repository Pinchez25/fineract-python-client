# PostLoansLoanIdCollateralsRequest

PostLoansLoanIdCollateralsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_type_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_collaterals_request import PostLoansLoanIdCollateralsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdCollateralsRequest from a JSON string
post_loans_loan_id_collaterals_request_instance = PostLoansLoanIdCollateralsRequest.from_json(json)
# print the JSON string representation of the object
print PostLoansLoanIdCollateralsRequest.to_json()

# convert the object into a dict
post_loans_loan_id_collaterals_request_dict = post_loans_loan_id_collaterals_request_instance.to_dict()
# create an instance of PostLoansLoanIdCollateralsRequest from a dict
post_loans_loan_id_collaterals_request_form_dict = post_loans_loan_id_collaterals_request.from_dict(post_loans_loan_id_collaterals_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


