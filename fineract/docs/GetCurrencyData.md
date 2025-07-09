# GetCurrencyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**decimal_places** | **int** |  | [optional] 
**display_label** | **str** |  | [optional] 
**display_symbol** | **str** |  | [optional] 
**in_multiples_of** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_currency_data import GetCurrencyData

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrencyData from a JSON string
get_currency_data_instance = GetCurrencyData.from_json(json)
# print the JSON string representation of the object
print GetCurrencyData.to_json()

# convert the object into a dict
get_currency_data_dict = get_currency_data_instance.to_dict()
# create an instance of GetCurrencyData from a dict
get_currency_data_form_dict = get_currency_data.from_dict(get_currency_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


