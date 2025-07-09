# PostInterestRateChartsChartIdChartSlabsRequest

PostInterestRateChartsChartIdChartSlabsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_interest_rate** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**from_period** | **int** |  | [optional] 
**incentives** | [**List[PostInterestRateChartsChartIdChartSlabsIncentives]**](PostInterestRateChartsChartIdChartSlabsIncentives.md) |  | [optional] 
**locale** | **str** |  | [optional] 
**period_type** | **int** |  | [optional] 
**to_period** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_interest_rate_charts_chart_id_chart_slabs_request import PostInterestRateChartsChartIdChartSlabsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostInterestRateChartsChartIdChartSlabsRequest from a JSON string
post_interest_rate_charts_chart_id_chart_slabs_request_instance = PostInterestRateChartsChartIdChartSlabsRequest.from_json(json)
# print the JSON string representation of the object
print(PostInterestRateChartsChartIdChartSlabsRequest.to_json())

# convert the object into a dict
post_interest_rate_charts_chart_id_chart_slabs_request_dict = post_interest_rate_charts_chart_id_chart_slabs_request_instance.to_dict()
# create an instance of PostInterestRateChartsChartIdChartSlabsRequest from a dict
post_interest_rate_charts_chart_id_chart_slabs_request_from_dict = PostInterestRateChartsChartIdChartSlabsRequest.from_dict(post_interest_rate_charts_chart_id_chart_slabs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


