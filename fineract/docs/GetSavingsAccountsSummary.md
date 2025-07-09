# GetSavingsAccountsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **float** |  | [optional] 
**available_balance** | **float** |  | [optional] 
**currency** | [**GetSavingsCurrency**](GetSavingsCurrency.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_accounts_summary import GetSavingsAccountsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsAccountsSummary from a JSON string
get_savings_accounts_summary_instance = GetSavingsAccountsSummary.from_json(json)
# print the JSON string representation of the object
print(GetSavingsAccountsSummary.to_json())

# convert the object into a dict
get_savings_accounts_summary_dict = get_savings_accounts_summary_instance.to_dict()
# create an instance of GetSavingsAccountsSummary from a dict
get_savings_accounts_summary_from_dict = GetSavingsAccountsSummary.from_dict(get_savings_accounts_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


