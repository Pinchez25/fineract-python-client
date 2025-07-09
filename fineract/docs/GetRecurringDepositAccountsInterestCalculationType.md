# GetRecurringDepositAccountsInterestCalculationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_accounts_interest_calculation_type import GetRecurringDepositAccountsInterestCalculationType

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositAccountsInterestCalculationType from a JSON string
get_recurring_deposit_accounts_interest_calculation_type_instance = GetRecurringDepositAccountsInterestCalculationType.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositAccountsInterestCalculationType.to_json()

# convert the object into a dict
get_recurring_deposit_accounts_interest_calculation_type_dict = get_recurring_deposit_accounts_interest_calculation_type_instance.to_dict()
# create an instance of GetRecurringDepositAccountsInterestCalculationType from a dict
get_recurring_deposit_accounts_interest_calculation_type_form_dict = get_recurring_deposit_accounts_interest_calculation_type.from_dict(get_recurring_deposit_accounts_interest_calculation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


