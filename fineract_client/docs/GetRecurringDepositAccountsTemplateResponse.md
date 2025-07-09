# GetRecurringDepositAccountsTemplateResponse

GetRecurringDepositAccountsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**product_options** | [**List[GetRecurringProductOptions]**](GetRecurringProductOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_accounts_template_response import GetRecurringDepositAccountsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositAccountsTemplateResponse from a JSON string
get_recurring_deposit_accounts_template_response_instance = GetRecurringDepositAccountsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetRecurringDepositAccountsTemplateResponse.to_json())

# convert the object into a dict
get_recurring_deposit_accounts_template_response_dict = get_recurring_deposit_accounts_template_response_instance.to_dict()
# create an instance of GetRecurringDepositAccountsTemplateResponse from a dict
get_recurring_deposit_accounts_template_response_from_dict = GetRecurringDepositAccountsTemplateResponse.from_dict(get_recurring_deposit_accounts_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


