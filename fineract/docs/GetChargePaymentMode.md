# GetChargePaymentMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_charge_payment_mode import GetChargePaymentMode

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargePaymentMode from a JSON string
get_charge_payment_mode_instance = GetChargePaymentMode.from_json(json)
# print the JSON string representation of the object
print GetChargePaymentMode.to_json()

# convert the object into a dict
get_charge_payment_mode_dict = get_charge_payment_mode_instance.to_dict()
# create an instance of GetChargePaymentMode from a dict
get_charge_payment_mode_form_dict = get_charge_payment_mode.from_dict(get_charge_payment_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


