# PutRecurringDepositProductsChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_recurring_deposit_products_changes import PutRecurringDepositProductsChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutRecurringDepositProductsChanges from a JSON string
put_recurring_deposit_products_changes_instance = PutRecurringDepositProductsChanges.from_json(json)
# print the JSON string representation of the object
print PutRecurringDepositProductsChanges.to_json()

# convert the object into a dict
put_recurring_deposit_products_changes_dict = put_recurring_deposit_products_changes_instance.to_dict()
# create an instance of PutRecurringDepositProductsChanges from a dict
put_recurring_deposit_products_changes_form_dict = put_recurring_deposit_products_changes.from_dict(put_recurring_deposit_products_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


