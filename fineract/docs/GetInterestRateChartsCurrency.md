# GetInterestRateChartsCurrency


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
from fineract_client.models.get_interest_rate_charts_currency import GetInterestRateChartsCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetInterestRateChartsCurrency from a JSON string
get_interest_rate_charts_currency_instance = GetInterestRateChartsCurrency.from_json(json)
# print the JSON string representation of the object
print GetInterestRateChartsCurrency.to_json()

# convert the object into a dict
get_interest_rate_charts_currency_dict = get_interest_rate_charts_currency_instance.to_dict()
# create an instance of GetInterestRateChartsCurrency from a dict
get_interest_rate_charts_currency_form_dict = get_interest_rate_charts_currency.from_dict(get_interest_rate_charts_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


