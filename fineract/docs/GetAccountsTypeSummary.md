# GetAccountsTypeSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**GetAccountsChargesCurrency**](GetAccountsChargesCurrency.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_type_summary import GetAccountsTypeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsTypeSummary from a JSON string
get_accounts_type_summary_instance = GetAccountsTypeSummary.from_json(json)
# print the JSON string representation of the object
print(GetAccountsTypeSummary.to_json())

# convert the object into a dict
get_accounts_type_summary_dict = get_accounts_type_summary_instance.to_dict()
# create an instance of GetAccountsTypeSummary from a dict
get_accounts_type_summary_from_dict = GetAccountsTypeSummary.from_dict(get_accounts_type_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


