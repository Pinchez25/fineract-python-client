# PostLoansLoanIdChanges

PostLoansLoanIdChanges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_on_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**status** | [**PostLoansLoanIdStatus**](PostLoansLoanIdStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.post_loans_loan_id_changes import PostLoansLoanIdChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoansLoanIdChanges from a JSON string
post_loans_loan_id_changes_instance = PostLoansLoanIdChanges.from_json(json)
# print the JSON string representation of the object
print PostLoansLoanIdChanges.to_json()

# convert the object into a dict
post_loans_loan_id_changes_dict = post_loans_loan_id_changes_instance.to_dict()
# create an instance of PostLoansLoanIdChanges from a dict
post_loans_loan_id_changes_form_dict = post_loans_loan_id_changes.from_dict(post_loans_loan_id_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


