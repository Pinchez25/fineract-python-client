# PutLoanChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | [optional] 
**principal** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.put_loan_changes import PutLoanChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutLoanChanges from a JSON string
put_loan_changes_instance = PutLoanChanges.from_json(json)
# print the JSON string representation of the object
print PutLoanChanges.to_json()

# convert the object into a dict
put_loan_changes_dict = put_loan_changes_instance.to_dict()
# create an instance of PutLoanChanges from a dict
put_loan_changes_form_dict = put_loan_changes.from_dict(put_loan_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


