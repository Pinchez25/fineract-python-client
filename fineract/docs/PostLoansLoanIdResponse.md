# PostLoansLoanIdResponse

PostLoansLoanIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PostLoansLoanIdChanges**](PostLoansLoanIdChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_external_id** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**sub_resource_external_id** | **str** |  | [optional] 
**sub_resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_response import PostLoansLoanIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdResponse from a JSON string
post_loans_loan_id_response_instance = PostLoansLoanIdResponse.from_json(json)
# print the JSON string representation of the object
print(PostLoansLoanIdResponse.to_json())

# convert the object into a dict
post_loans_loan_id_response_dict = post_loans_loan_id_response_instance.to_dict()
# create an instance of PostLoansLoanIdResponse from a dict
post_loans_loan_id_response_from_dict = PostLoansLoanIdResponse.from_dict(post_loans_loan_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


