# GetTransactionsCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**decimal_places** | **int** |  | [optional] 
**display_label** | **str** |  | [optional] 
**display_symbol** | **str** |  | [optional] 
**is_multiples_of** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_code** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_transactions_currency import GetTransactionsCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionsCurrency from a JSON string
get_transactions_currency_instance = GetTransactionsCurrency.from_json(json)
# print the JSON string representation of the object
print GetTransactionsCurrency.to_json()

# convert the object into a dict
get_transactions_currency_dict = get_transactions_currency_instance.to_dict()
# create an instance of GetTransactionsCurrency from a dict
get_transactions_currency_form_dict = get_transactions_currency.from_dict(get_transactions_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


