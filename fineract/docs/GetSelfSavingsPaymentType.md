# GetSelfSavingsPaymentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_savings_payment_type import GetSelfSavingsPaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfSavingsPaymentType from a JSON string
get_self_savings_payment_type_instance = GetSelfSavingsPaymentType.from_json(json)
# print the JSON string representation of the object
print GetSelfSavingsPaymentType.to_json()

# convert the object into a dict
get_self_savings_payment_type_dict = get_self_savings_payment_type_instance.to_dict()
# create an instance of GetSelfSavingsPaymentType from a dict
get_self_savings_payment_type_form_dict = get_self_savings_payment_type.from_dict(get_self_savings_payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


