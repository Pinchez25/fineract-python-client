# GetRecurringDepositProductsInterestCalculationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_deposit_products_interest_calculation_type import GetRecurringDepositProductsInterestCalculationType

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringDepositProductsInterestCalculationType from a JSON string
get_recurring_deposit_products_interest_calculation_type_instance = GetRecurringDepositProductsInterestCalculationType.from_json(json)
# print the JSON string representation of the object
print GetRecurringDepositProductsInterestCalculationType.to_json()

# convert the object into a dict
get_recurring_deposit_products_interest_calculation_type_dict = get_recurring_deposit_products_interest_calculation_type_instance.to_dict()
# create an instance of GetRecurringDepositProductsInterestCalculationType from a dict
get_recurring_deposit_products_interest_calculation_type_form_dict = get_recurring_deposit_products_interest_calculation_type.from_dict(get_recurring_deposit_products_interest_calculation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


