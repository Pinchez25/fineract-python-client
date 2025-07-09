# GetChargesTemplateResponse

GetChargesTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**charge_applies_to_options** | [**List[GetChargesAppliesToResponse]**](GetChargesAppliesToResponse.md) |  | [optional] 
**charge_calculation_type_options** | [**List[GetChargesCalculationTypeResponse]**](GetChargesCalculationTypeResponse.md) |  | [optional] 
**charge_payment_mode_options** | [**List[GetChargesPaymentModeResponse]**](GetChargesPaymentModeResponse.md) |  | [optional] 
**charge_time_type_options** | [**List[GetChargesTimeTypeResponse]**](GetChargesTimeTypeResponse.md) |  | [optional] 
**currency_options** | [**List[GetChargesCurrencyResponse]**](GetChargesCurrencyResponse.md) |  | [optional] 
**fee_frequency_options** | [**List[GetChargesTemplateFeeFrequencyOptions]**](GetChargesTemplateFeeFrequencyOptions.md) |  | [optional] 
**loan_charge_calculation_type_options** | [**List[GetChargesTemplateLoanChargeCalculationTypeOptions]**](GetChargesTemplateLoanChargeCalculationTypeOptions.md) |  | [optional] 
**loan_charge_time_type_options** | [**List[GetChargesTemplateLoanChargeTimeTypeOptions]**](GetChargesTemplateLoanChargeTimeTypeOptions.md) |  | [optional] 
**penalty** | **bool** |  | [optional] 
**savings_charge_calculation_type_options** | [**List[GetChargesTemplateLoanChargeCalculationTypeOptions]**](GetChargesTemplateLoanChargeCalculationTypeOptions.md) |  | [optional] 
**savings_charge_time_type_options** | [**List[GetChargesTemplateLoanChargeTimeTypeOptions]**](GetChargesTemplateLoanChargeTimeTypeOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_charges_template_response import GetChargesTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargesTemplateResponse from a JSON string
get_charges_template_response_instance = GetChargesTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetChargesTemplateResponse.to_json()

# convert the object into a dict
get_charges_template_response_dict = get_charges_template_response_instance.to_dict()
# create an instance of GetChargesTemplateResponse from a dict
get_charges_template_response_form_dict = get_charges_template_response.from_dict(get_charges_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


