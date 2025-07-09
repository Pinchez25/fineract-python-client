# PostFloatingRatesRequest

PostFloatingRatesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional] 
**is_base_lending_rate** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**rate_periods** | [**List[PostFloatingRatesRatePeriods]**](PostFloatingRatesRatePeriods.md) |  | [optional] 

## Example

```python
from fineract_client.models.post_floating_rates_request import PostFloatingRatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFloatingRatesRequest from a JSON string
post_floating_rates_request_instance = PostFloatingRatesRequest.from_json(json)
# print the JSON string representation of the object
print(PostFloatingRatesRequest.to_json())

# convert the object into a dict
post_floating_rates_request_dict = post_floating_rates_request_instance.to_dict()
# create an instance of PostFloatingRatesRequest from a dict
post_floating_rates_request_from_dict = PostFloatingRatesRequest.from_dict(post_floating_rates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


