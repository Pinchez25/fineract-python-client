# GetChargesTemplateFeeFrequencyOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_charges_template_fee_frequency_options import GetChargesTemplateFeeFrequencyOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargesTemplateFeeFrequencyOptions from a JSON string
get_charges_template_fee_frequency_options_instance = GetChargesTemplateFeeFrequencyOptions.from_json(json)
# print the JSON string representation of the object
print(GetChargesTemplateFeeFrequencyOptions.to_json())

# convert the object into a dict
get_charges_template_fee_frequency_options_dict = get_charges_template_fee_frequency_options_instance.to_dict()
# create an instance of GetChargesTemplateFeeFrequencyOptions from a dict
get_charges_template_fee_frequency_options_from_dict = GetChargesTemplateFeeFrequencyOptions.from_dict(get_charges_template_fee_frequency_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


