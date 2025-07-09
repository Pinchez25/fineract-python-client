# PostSelfLoansLoanIdChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_on_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**status** | [**PostSelfLoansLoanIdStatus**](PostSelfLoansLoanIdStatus.md) |  | [optional] 
**withdrawn_on_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_self_loans_loan_id_changes import PostSelfLoansLoanIdChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PostSelfLoansLoanIdChanges from a JSON string
post_self_loans_loan_id_changes_instance = PostSelfLoansLoanIdChanges.from_json(json)
# print the JSON string representation of the object
print PostSelfLoansLoanIdChanges.to_json()

# convert the object into a dict
post_self_loans_loan_id_changes_dict = post_self_loans_loan_id_changes_instance.to_dict()
# create an instance of PostSelfLoansLoanIdChanges from a dict
post_self_loans_loan_id_changes_form_dict = post_self_loans_loan_id_changes.from_dict(post_self_loans_loan_id_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


