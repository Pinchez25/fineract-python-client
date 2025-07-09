# PutSelfLoansChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | [optional] 
**principal** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_self_loans_changes import PutSelfLoansChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutSelfLoansChanges from a JSON string
put_self_loans_changes_instance = PutSelfLoansChanges.from_json(json)
# print the JSON string representation of the object
print PutSelfLoansChanges.to_json()

# convert the object into a dict
put_self_loans_changes_dict = put_self_loans_changes_instance.to_dict()
# create an instance of PutSelfLoansChanges from a dict
put_self_loans_changes_form_dict = put_self_loans_changes.from_dict(put_self_loans_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


