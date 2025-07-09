# Money


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**amount_defaulted_to_null_if_zero** | **float** |  | [optional] 
**currency** | [**MonetaryCurrency**](MonetaryCurrency.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**currency_digits_after_decimal** | **int** |  | [optional] 
**currency_in_multiples_of** | **int** |  | [optional] 
**greater_than_zero** | **bool** |  | [optional] 
**less_than_zero** | **bool** |  | [optional] 
**zero** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.money import Money

# TODO update the JSON string below
json = "{}"
# create an instance of Money from a JSON string
money_instance = Money.from_json(json)
# print the JSON string representation of the object
print Money.to_json()

# convert the object into a dict
money_dict = money_instance.to_dict()
# create an instance of Money from a dict
money_form_dict = money.from_dict(money_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


