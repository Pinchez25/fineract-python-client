# GetLoansChargePaymentMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_charge_payment_mode import GetLoansChargePaymentMode

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansChargePaymentMode from a JSON string
get_loans_charge_payment_mode_instance = GetLoansChargePaymentMode.from_json(json)
# print the JSON string representation of the object
print(GetLoansChargePaymentMode.to_json())

# convert the object into a dict
get_loans_charge_payment_mode_dict = get_loans_charge_payment_mode_instance.to_dict()
# create an instance of GetLoansChargePaymentMode from a dict
get_loans_charge_payment_mode_from_dict = GetLoansChargePaymentMode.from_dict(get_loans_charge_payment_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


