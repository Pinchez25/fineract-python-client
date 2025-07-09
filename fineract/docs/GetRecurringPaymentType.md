# GetRecurringPaymentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_recurring_payment_type import GetRecurringPaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecurringPaymentType from a JSON string
get_recurring_payment_type_instance = GetRecurringPaymentType.from_json(json)
# print the JSON string representation of the object
print(GetRecurringPaymentType.to_json())

# convert the object into a dict
get_recurring_payment_type_dict = get_recurring_payment_type_instance.to_dict()
# create an instance of GetRecurringPaymentType from a dict
get_recurring_payment_type_from_dict = GetRecurringPaymentType.from_dict(get_recurring_payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


