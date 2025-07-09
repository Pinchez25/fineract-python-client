# PutAccountsChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**requested_shares** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_accounts_changes import PutAccountsChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutAccountsChanges from a JSON string
put_accounts_changes_instance = PutAccountsChanges.from_json(json)
# print the JSON string representation of the object
print PutAccountsChanges.to_json()

# convert the object into a dict
put_accounts_changes_dict = put_accounts_changes_instance.to_dict()
# create an instance of PutAccountsChanges from a dict
put_accounts_changes_form_dict = put_accounts_changes.from_dict(put_accounts_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


