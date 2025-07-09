# GetRecurringDepositAccountsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_balance** | **float** |  | [optional] 
**currency** | [**GetRecurringDepositAccountsCurrency**](GetRecurringDepositAccountsCurrency.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_accounts_summary import GetRecurringDepositAccountsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositAccountsSummary from a JSON string
get_recurring_deposit_accounts_summary_instance = GetRecurringDepositAccountsSummary.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositAccountsSummary.to_json()

# convert the object into a dict
get_recurring_deposit_accounts_summary_dict = get_recurring_deposit_accounts_summary_instance.to_dict()
# create an instance of GetRecurringDepositAccountsSummary from a dict
get_recurring_deposit_accounts_summary_form_dict = get_recurring_deposit_accounts_summary.from_dict(get_recurring_deposit_accounts_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


