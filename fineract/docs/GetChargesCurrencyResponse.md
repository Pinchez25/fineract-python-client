# GetChargesCurrencyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**decimal_places** | **int** |  | [optional] 
**display_label** | **str** |  | [optional] 
**display_symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**name_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_charges_currency_response import GetChargesCurrencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargesCurrencyResponse from a JSON string
get_charges_currency_response_instance = GetChargesCurrencyResponse.from_json(json)
# print the JSON string representation of the object
print GetChargesCurrencyResponse.to_json()

# convert the object into a dict
get_charges_currency_response_dict = get_charges_currency_response_instance.to_dict()
# create an instance of GetChargesCurrencyResponse from a dict
get_charges_currency_response_form_dict = get_charges_currency_response.from_dict(get_charges_currency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


