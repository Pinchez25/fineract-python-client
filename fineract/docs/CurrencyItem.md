# CurrencyItem


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
from fineract_client.models.currency_item import CurrencyItem

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyItem from a JSON string
currency_item_instance = CurrencyItem.from_json(json)
# print the JSON string representation of the object
print(CurrencyItem.to_json())

# convert the object into a dict
currency_item_dict = currency_item_instance.to_dict()
# create an instance of CurrencyItem from a dict
currency_item_from_dict = CurrencyItem.from_dict(currency_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


