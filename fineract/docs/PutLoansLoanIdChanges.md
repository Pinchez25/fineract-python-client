# PutLoansLoanIdChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fraud** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**principal** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_loans_loan_id_changes import PutLoansLoanIdChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutLoansLoanIdChanges from a JSON string
put_loans_loan_id_changes_instance = PutLoansLoanIdChanges.from_json(json)
# print the JSON string representation of the object
print PutLoansLoanIdChanges.to_json()

# convert the object into a dict
put_loans_loan_id_changes_dict = put_loans_loan_id_changes_instance.to_dict()
# create an instance of PutLoansLoanIdChanges from a dict
put_loans_loan_id_changes_form_dict = put_loans_loan_id_changes.from_dict(put_loans_loan_id_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


