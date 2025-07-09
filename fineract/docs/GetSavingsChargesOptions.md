# GetSavingsChargesOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**amount** | **float** |  | [optional] 
**charge_calculation_type** | [**GetChargesChargeCalculationType**](GetChargesChargeCalculationType.md) |  | [optional] 
**charge_time_type** | [**GetSavingsChargesChargeTimeType**](GetSavingsChargesChargeTimeType.md) |  | [optional] 
**charges_applies_to** | [**GetChargesAppliesTo**](GetChargesAppliesTo.md) |  | [optional] 
**currency** | [**GetChargesCurrencyResponse**](GetChargesCurrencyResponse.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_charges_options import GetSavingsChargesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsChargesOptions from a JSON string
get_savings_charges_options_instance = GetSavingsChargesOptions.from_json(json)
# print the JSON string representation of the object
print GetSavingsChargesOptions.to_json()

# convert the object into a dict
get_savings_charges_options_dict = get_savings_charges_options_instance.to_dict()
# create an instance of GetSavingsChargesOptions from a dict
get_savings_charges_options_form_dict = get_savings_charges_options.from_dict(get_savings_charges_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


