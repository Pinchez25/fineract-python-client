# PostLoansLoanIdDisbursementData

List of PostLoansLoanIdDisbursementData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_disbursement_date** | **date** |  | [optional] 
**principal** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_disbursement_data import PostLoansLoanIdDisbursementData

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdDisbursementData from a JSON string
post_loans_loan_id_disbursement_data_instance = PostLoansLoanIdDisbursementData.from_json(json)
# print the JSON string representation of the object
print(PostLoansLoanIdDisbursementData.to_json())

# convert the object into a dict
post_loans_loan_id_disbursement_data_dict = post_loans_loan_id_disbursement_data_instance.to_dict()
# create an instance of PostLoansLoanIdDisbursementData from a dict
post_loans_loan_id_disbursement_data_from_dict = PostLoansLoanIdDisbursementData.from_dict(post_loans_loan_id_disbursement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


