# PostLoansLoanIdChargesResponse

 PostLoansLoanIdChargesResponse

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
from fineract_client.models.post_loans_loan_id_charges_response import PostLoansLoanIdChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdChargesResponse from a JSON string
post_loans_loan_id_charges_response_instance = PostLoansLoanIdChargesResponse.from_json(json)
# print the JSON string representation of the object
print PostLoansLoanIdChargesResponse.to_json()

# convert the object into a dict
post_loans_loan_id_charges_response_dict = post_loans_loan_id_charges_response_instance.to_dict()
# create an instance of PostLoansLoanIdChargesResponse from a dict
post_loans_loan_id_charges_response_form_dict = post_loans_loan_id_charges_response.from_dict(post_loans_loan_id_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


