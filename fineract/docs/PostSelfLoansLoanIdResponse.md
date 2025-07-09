# PostSelfLoansLoanIdResponse

PostSelfLoansLoanIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PostSelfLoansLoanIdChanges**](PostSelfLoansLoanIdChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_self_loans_loan_id_response import PostSelfLoansLoanIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostSelfLoansLoanIdResponse from a JSON string
post_self_loans_loan_id_response_instance = PostSelfLoansLoanIdResponse.from_json(json)
# print the JSON string representation of the object
print PostSelfLoansLoanIdResponse.to_json()

# convert the object into a dict
post_self_loans_loan_id_response_dict = post_self_loans_loan_id_response_instance.to_dict()
# create an instance of PostSelfLoansLoanIdResponse from a dict
post_self_loans_loan_id_response_form_dict = post_self_loans_loan_id_response.from_dict(post_self_loans_loan_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


