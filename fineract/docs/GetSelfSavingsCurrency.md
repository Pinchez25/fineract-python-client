# GetSelfSavingsCurrency


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
from fineract_client.models.get_self_savings_currency import GetSelfSavingsCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfSavingsCurrency from a JSON string
get_self_savings_currency_instance = GetSelfSavingsCurrency.from_json(json)
# print the JSON string representation of the object
print(GetSelfSavingsCurrency.to_json())

# convert the object into a dict
get_self_savings_currency_dict = get_self_savings_currency_instance.to_dict()
# create an instance of GetSelfSavingsCurrency from a dict
get_self_savings_currency_from_dict = GetSelfSavingsCurrency.from_dict(get_self_savings_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


