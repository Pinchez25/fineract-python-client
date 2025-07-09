# PostLoansLoanIdChargesRequest

 PostLoansLoanIdChargesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**charge_id** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_charges_request import PostLoansLoanIdChargesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdChargesRequest from a JSON string
post_loans_loan_id_charges_request_instance = PostLoansLoanIdChargesRequest.from_json(json)
# print the JSON string representation of the object
print(PostLoansLoanIdChargesRequest.to_json())

# convert the object into a dict
post_loans_loan_id_charges_request_dict = post_loans_loan_id_charges_request_instance.to_dict()
# create an instance of PostLoansLoanIdChargesRequest from a dict
post_loans_loan_id_charges_request_from_dict = PostLoansLoanIdChargesRequest.from_dict(post_loans_loan_id_charges_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


