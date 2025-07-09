# GetChargesResponse

GetChargesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**amount** | **float** |  | [optional] 
**charge_applies_to** | [**GetChargesAppliesToResponse**](GetChargesAppliesToResponse.md) |  | [optional] 
**charge_calculation_type** | [**GetChargesCalculationTypeResponse**](GetChargesCalculationTypeResponse.md) |  | [optional] 
**charge_payment_mode** | [**GetChargesPaymentModeResponse**](GetChargesPaymentModeResponse.md) |  | [optional] 
**charge_time_type** | [**GetChargesTimeTypeResponse**](GetChargesTimeTypeResponse.md) |  | [optional] 
**currency** | [**GetChargesCurrencyResponse**](GetChargesCurrencyResponse.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_charges_response import GetChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargesResponse from a JSON string
get_charges_response_instance = GetChargesResponse.from_json(json)
# print the JSON string representation of the object
print GetChargesResponse.to_json()

# convert the object into a dict
get_charges_response_dict = get_charges_response_instance.to_dict()
# create an instance of GetChargesResponse from a dict
get_charges_response_form_dict = get_charges_response.from_dict(get_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


