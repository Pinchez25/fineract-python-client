# PostLoanChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**removed_entity_ids** | **List[int]** |  | [optional] 

## Example

```python
from fineract_client.models.post_loan_changes import PostLoanChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PostLoanChanges from a JSON string
post_loan_changes_instance = PostLoanChanges.from_json(json)
# print the JSON string representation of the object
print PostLoanChanges.to_json()

# convert the object into a dict
post_loan_changes_dict = post_loan_changes_instance.to_dict()
# create an instance of PostLoanChanges from a dict
post_loan_changes_form_dict = post_loan_changes.from_dict(post_loan_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


