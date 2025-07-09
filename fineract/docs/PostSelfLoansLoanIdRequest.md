# PostSelfLoansLoanIdRequest

PostSelfLoansLoanIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**withdrawn_on_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_self_loans_loan_id_request import PostSelfLoansLoanIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSelfLoansLoanIdRequest from a JSON string
post_self_loans_loan_id_request_instance = PostSelfLoansLoanIdRequest.from_json(json)
# print the JSON string representation of the object
print PostSelfLoansLoanIdRequest.to_json()

# convert the object into a dict
post_self_loans_loan_id_request_dict = post_self_loans_loan_id_request_instance.to_dict()
# create an instance of PostSelfLoansLoanIdRequest from a dict
post_self_loans_loan_id_request_form_dict = post_self_loans_loan_id_request.from_dict(post_self_loans_loan_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


