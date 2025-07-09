# CurrencyData


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
from fineract_client.models.currency_data import CurrencyData

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyData from a JSON string
currency_data_instance = CurrencyData.from_json(json)
# print the JSON string representation of the object
print CurrencyData.to_json()

# convert the object into a dict
currency_data_dict = currency_data_instance.to_dict()
# create an instance of CurrencyData from a dict
currency_data_form_dict = currency_data.from_dict(currency_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


