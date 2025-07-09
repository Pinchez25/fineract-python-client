# AllowAttributeOverrides


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amortization_type** | **bool** |  | [optional] 
**grace_on_arrears_ageing** | **bool** |  | [optional] 
**grace_on_principal_and_interest_payment** | **bool** |  | [optional] 
**in_arrears_tolerance** | **bool** |  | [optional] 
**interest_calculation_period_type** | **bool** |  | [optional] 
**interest_type** | **bool** |  | [optional] 
**repayment_every** | **bool** |  | [optional] 
**transaction_processing_strategy_code** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.allow_attribute_overrides import AllowAttributeOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of AllowAttributeOverrides from a JSON string
allow_attribute_overrides_instance = AllowAttributeOverrides.from_json(json)
# print the JSON string representation of the object
print AllowAttributeOverrides.to_json()

# convert the object into a dict
allow_attribute_overrides_dict = allow_attribute_overrides_instance.to_dict()
# create an instance of AllowAttributeOverrides from a dict
allow_attribute_overrides_form_dict = allow_attribute_overrides.from_dict(allow_attribute_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


