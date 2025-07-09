# GetFloatingRatesRatePeriods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**from_date** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_differential_to_base_lending_rate** | **bool** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_floating_rates_rate_periods import GetFloatingRatesRatePeriods

# TODO update the JSON string below
json = "{}"
# create an instance of GetFloatingRatesRatePeriods from a JSON string
get_floating_rates_rate_periods_instance = GetFloatingRatesRatePeriods.from_json(json)
# print the JSON string representation of the object
print GetFloatingRatesRatePeriods.to_json()

# convert the object into a dict
get_floating_rates_rate_periods_dict = get_floating_rates_rate_periods_instance.to_dict()
# create an instance of GetFloatingRatesRatePeriods from a dict
get_floating_rates_rate_periods_form_dict = get_floating_rates_rate_periods.from_dict(get_floating_rates_rate_periods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


