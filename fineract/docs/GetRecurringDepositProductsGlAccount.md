# GetRecurringDepositProductsGlAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_products_gl_account import GetRecurringDepositProductsGlAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositProductsGlAccount from a JSON string
get_recurring_deposit_products_gl_account_instance = GetRecurringDepositProductsGlAccount.from_json(json)
# print the JSON string representation of the object
print(GetRecurringDepositProductsGlAccount.to_json())

# convert the object into a dict
get_recurring_deposit_products_gl_account_dict = get_recurring_deposit_products_gl_account_instance.to_dict()
# create an instance of GetRecurringDepositProductsGlAccount from a dict
get_recurring_deposit_products_gl_account_from_dict = GetRecurringDepositProductsGlAccount.from_dict(get_recurring_deposit_products_gl_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


