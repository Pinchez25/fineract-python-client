# GetInterestRateChartsTemplateResponse

GetInterestRateChartsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_types** | [**List[GetInterestRateChartsTemplatePeriodTypes]**](GetInterestRateChartsTemplatePeriodTypes.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_interest_rate_charts_template_response import GetInterestRateChartsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInterestRateChartsTemplateResponse from a JSON string
get_interest_rate_charts_template_response_instance = GetInterestRateChartsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetInterestRateChartsTemplateResponse.to_json()

# convert the object into a dict
get_interest_rate_charts_template_response_dict = get_interest_rate_charts_template_response_instance.to_dict()
# create an instance of GetInterestRateChartsTemplateResponse from a dict
get_interest_rate_charts_template_response_form_dict = get_interest_rate_charts_template_response.from_dict(get_interest_rate_charts_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


