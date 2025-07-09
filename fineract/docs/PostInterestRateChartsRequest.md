# PostInterestRateChartsRequest

PostInterestRateChartsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**from_date** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_interest_rate_charts_request import PostInterestRateChartsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostInterestRateChartsRequest from a JSON string
post_interest_rate_charts_request_instance = PostInterestRateChartsRequest.from_json(json)
# print the JSON string representation of the object
print PostInterestRateChartsRequest.to_json()

# convert the object into a dict
post_interest_rate_charts_request_dict = post_interest_rate_charts_request_instance.to_dict()
# create an instance of PostInterestRateChartsRequest from a dict
post_interest_rate_charts_request_form_dict = post_interest_rate_charts_request.from_dict(post_interest_rate_charts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


