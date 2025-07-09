# GetInterestRateChartsChartIdChartSlabsResponse

GetInterestRateChartsChartIdChartSlabsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_interest_rate** | **float** |  | [optional] 
**currency** | [**GetInterestRateChartsCurrency**](GetInterestRateChartsCurrency.md) |  | [optional] 
**description** | **str** |  | [optional] 
**from_period** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**incentives** | [**List[GetInterestRateChartsChartIdChartSlabsIncentives]**](GetInterestRateChartsChartIdChartSlabsIncentives.md) |  | [optional] 
**period_types** | [**GetInterestRateChartsTemplatePeriodTypes**](GetInterestRateChartsTemplatePeriodTypes.md) |  | [optional] 
**to_period** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_interest_rate_charts_chart_id_chart_slabs_response import GetInterestRateChartsChartIdChartSlabsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInterestRateChartsChartIdChartSlabsResponse from a JSON string
get_interest_rate_charts_chart_id_chart_slabs_response_instance = GetInterestRateChartsChartIdChartSlabsResponse.from_json(json)
# print the JSON string representation of the object
print(GetInterestRateChartsChartIdChartSlabsResponse.to_json())

# convert the object into a dict
get_interest_rate_charts_chart_id_chart_slabs_response_dict = get_interest_rate_charts_chart_id_chart_slabs_response_instance.to_dict()
# create an instance of GetInterestRateChartsChartIdChartSlabsResponse from a dict
get_interest_rate_charts_chart_id_chart_slabs_response_from_dict = GetInterestRateChartsChartIdChartSlabsResponse.from_dict(get_interest_rate_charts_chart_id_chart_slabs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


