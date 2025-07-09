# GetClientTransactionsCurrency


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
from fineract_client.models.get_client_transactions_currency import GetClientTransactionsCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientTransactionsCurrency from a JSON string
get_client_transactions_currency_instance = GetClientTransactionsCurrency.from_json(json)
# print the JSON string representation of the object
print(GetClientTransactionsCurrency.to_json())

# convert the object into a dict
get_client_transactions_currency_dict = get_client_transactions_currency_instance.to_dict()
# create an instance of GetClientTransactionsCurrency from a dict
get_client_transactions_currency_from_dict = GetClientTransactionsCurrency.from_dict(get_client_transactions_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


