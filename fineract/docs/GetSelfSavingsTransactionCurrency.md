# GetSelfSavingsTransactionCurrency


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
from fineract_client.models.get_self_savings_transaction_currency import GetSelfSavingsTransactionCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfSavingsTransactionCurrency from a JSON string
get_self_savings_transaction_currency_instance = GetSelfSavingsTransactionCurrency.from_json(json)
# print the JSON string representation of the object
print(GetSelfSavingsTransactionCurrency.to_json())

# convert the object into a dict
get_self_savings_transaction_currency_dict = get_self_savings_transaction_currency_instance.to_dict()
# create an instance of GetSelfSavingsTransactionCurrency from a dict
get_self_savings_transaction_currency_from_dict = GetSelfSavingsTransactionCurrency.from_dict(get_self_savings_transaction_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


