# GetCurrenciesResponse

GetCurrenciesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_options** | [**List[CurrencyData]**](CurrencyData.md) |  | [optional] 
**selected_currency_options** | [**List[CurrencyData]**](CurrencyData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_currencies_response import GetCurrenciesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCurrenciesResponse from a JSON string
get_currencies_response_instance = GetCurrenciesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCurrenciesResponse.to_json())

# convert the object into a dict
get_currencies_response_dict = get_currencies_response_instance.to_dict()
# create an instance of GetCurrenciesResponse from a dict
get_currencies_response_from_dict = GetCurrenciesResponse.from_dict(get_currencies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


