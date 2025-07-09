# PutSavingsAccountsChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | [optional] 
**nominal_annual_interest_rate** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.put_savings_accounts_changes import PutSavingsAccountsChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutSavingsAccountsChanges from a JSON string
put_savings_accounts_changes_instance = PutSavingsAccountsChanges.from_json(json)
# print the JSON string representation of the object
print(PutSavingsAccountsChanges.to_json())

# convert the object into a dict
put_savings_accounts_changes_dict = put_savings_accounts_changes_instance.to_dict()
# create an instance of PutSavingsAccountsChanges from a dict
put_savings_accounts_changes_from_dict = PutSavingsAccountsChanges.from_dict(put_savings_accounts_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


