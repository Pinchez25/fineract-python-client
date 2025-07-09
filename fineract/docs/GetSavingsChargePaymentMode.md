# GetSavingsChargePaymentMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_charge_payment_mode import GetSavingsChargePaymentMode

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsChargePaymentMode from a JSON string
get_savings_charge_payment_mode_instance = GetSavingsChargePaymentMode.from_json(json)
# print the JSON string representation of the object
print GetSavingsChargePaymentMode.to_json()

# convert the object into a dict
get_savings_charge_payment_mode_dict = get_savings_charge_payment_mode_instance.to_dict()
# create an instance of GetSavingsChargePaymentMode from a dict
get_savings_charge_payment_mode_form_dict = get_savings_charge_payment_mode.from_dict(get_savings_charge_payment_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


