# GetInterestRateChartsChartIdChartSlabsIncentives


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**attribute_name** | [**GetInterestRateChartsChartIdChartSlabsAttributeName**](GetInterestRateChartsChartIdChartSlabsAttributeName.md) |  | [optional] 
**attribute_value** | **int** |  | [optional] 
**attribute_value_desc** | **str** |  | [optional] 
**condition_type** | [**GetInterestRateChartsChartIdChartSlabsConditionType**](GetInterestRateChartsChartIdChartSlabsConditionType.md) |  | [optional] 
**entity_type** | [**GetInterestRateChartsChartIdChartSlabsEntityType**](GetInterestRateChartsChartIdChartSlabsEntityType.md) |  | [optional] 
**id** | **int** |  | [optional] 
**incentive_type** | [**GetInterestRateChartsChartIdChartSlabsIncentiveType**](GetInterestRateChartsChartIdChartSlabsIncentiveType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_interest_rate_charts_chart_id_chart_slabs_incentives import GetInterestRateChartsChartIdChartSlabsIncentives

# TODO update the JSON string below
json = "{}"
# create an instance of GetInterestRateChartsChartIdChartSlabsIncentives from a JSON string
get_interest_rate_charts_chart_id_chart_slabs_incentives_instance = GetInterestRateChartsChartIdChartSlabsIncentives.from_json(json)
# print the JSON string representation of the object
print GetInterestRateChartsChartIdChartSlabsIncentives.to_json()

# convert the object into a dict
get_interest_rate_charts_chart_id_chart_slabs_incentives_dict = get_interest_rate_charts_chart_id_chart_slabs_incentives_instance.to_dict()
# create an instance of GetInterestRateChartsChartIdChartSlabsIncentives from a dict
get_interest_rate_charts_chart_id_chart_slabs_incentives_form_dict = get_interest_rate_charts_chart_id_chart_slabs_incentives.from_dict(get_interest_rate_charts_chart_id_chart_slabs_incentives_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


