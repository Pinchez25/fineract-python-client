# MonetaryCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**currency_in_multiples_of** | **int** |  | [optional] 
**digits_after_decimal** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.monetary_currency import MonetaryCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of MonetaryCurrency from a JSON string
monetary_currency_instance = MonetaryCurrency.from_json(json)
# print the JSON string representation of the object
print(MonetaryCurrency.to_json())

# convert the object into a dict
monetary_currency_dict = monetary_currency_instance.to_dict()
# create an instance of MonetaryCurrency from a dict
monetary_currency_from_dict = MonetaryCurrency.from_dict(monetary_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


