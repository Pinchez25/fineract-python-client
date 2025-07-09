# GetInterestRateChartsResponse

GetInterestRateChartsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_slabs** | [**List[GetInterestRateChartsChartSlabs]**](GetInterestRateChartsChartSlabs.md) |  | [optional] 
**from_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_interest_rate_charts_response import GetInterestRateChartsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInterestRateChartsResponse from a JSON string
get_interest_rate_charts_response_instance = GetInterestRateChartsResponse.from_json(json)
# print the JSON string representation of the object
print GetInterestRateChartsResponse.to_json()

# convert the object into a dict
get_interest_rate_charts_response_dict = get_interest_rate_charts_response_instance.to_dict()
# create an instance of GetInterestRateChartsResponse from a dict
get_interest_rate_charts_response_form_dict = get_interest_rate_charts_response.from_dict(get_interest_rate_charts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


