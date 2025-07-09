# PostFloatingRatesRatePeriods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**from_date** | **str** |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_floating_rates_rate_periods import PostFloatingRatesRatePeriods

# TODO update the JSON string below
json = "{}"
# create an instance of PostFloatingRatesRatePeriods from a JSON string
post_floating_rates_rate_periods_instance = PostFloatingRatesRatePeriods.from_json(json)
# print the JSON string representation of the object
print(PostFloatingRatesRatePeriods.to_json())

# convert the object into a dict
post_floating_rates_rate_periods_dict = post_floating_rates_rate_periods_instance.to_dict()
# create an instance of PostFloatingRatesRatePeriods from a dict
post_floating_rates_rate_periods_from_dict = PostFloatingRatesRatePeriods.from_dict(post_floating_rates_rate_periods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


