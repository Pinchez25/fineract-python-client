# GetInterestRateChartsChartSlabs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_interest_rate** | **int** |  | [optional] 
**currency** | [**GetInterestRateChartsCurrency**](GetInterestRateChartsCurrency.md) |  | [optional] 
**from_period** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**period_types** | [**GetInterestRateChartsTemplatePeriodTypes**](GetInterestRateChartsTemplatePeriodTypes.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_interest_rate_charts_chart_slabs import GetInterestRateChartsChartSlabs

# TODO update the JSON string below
json = "{}"
# create an instance of GetInterestRateChartsChartSlabs from a JSON string
get_interest_rate_charts_chart_slabs_instance = GetInterestRateChartsChartSlabs.from_json(json)
# print the JSON string representation of the object
print GetInterestRateChartsChartSlabs.to_json()

# convert the object into a dict
get_interest_rate_charts_chart_slabs_dict = get_interest_rate_charts_chart_slabs_instance.to_dict()
# create an instance of GetInterestRateChartsChartSlabs from a dict
get_interest_rate_charts_chart_slabs_form_dict = get_interest_rate_charts_chart_slabs.from_dict(get_interest_rate_charts_chart_slabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


