# GetRecurringDepositAccountsTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submitted_by_firstname** | **str** |  | [optional] 
**submitted_by_lastname** | **str** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_accounts_timeline import GetRecurringDepositAccountsTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositAccountsTimeline from a JSON string
get_recurring_deposit_accounts_timeline_instance = GetRecurringDepositAccountsTimeline.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositAccountsTimeline.to_json()

# convert the object into a dict
get_recurring_deposit_accounts_timeline_dict = get_recurring_deposit_accounts_timeline_instance.to_dict()
# create an instance of GetRecurringDepositAccountsTimeline from a dict
get_recurring_deposit_accounts_timeline_form_dict = get_recurring_deposit_accounts_timeline.from_dict(get_recurring_deposit_accounts_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


