# GetFloatingRatesFloatingRateIdResponse

GetFloatingRatesFloatingRateIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**created_on** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_base_lending_rate** | **bool** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**modified_on** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**rate_periods** | [**List[GetFloatingRatesRatePeriods]**](GetFloatingRatesRatePeriods.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_floating_rates_floating_rate_id_response import GetFloatingRatesFloatingRateIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFloatingRatesFloatingRateIdResponse from a JSON string
get_floating_rates_floating_rate_id_response_instance = GetFloatingRatesFloatingRateIdResponse.from_json(json)
# print the JSON string representation of the object
print GetFloatingRatesFloatingRateIdResponse.to_json()

# convert the object into a dict
get_floating_rates_floating_rate_id_response_dict = get_floating_rates_floating_rate_id_response_instance.to_dict()
# create an instance of GetFloatingRatesFloatingRateIdResponse from a dict
get_floating_rates_floating_rate_id_response_form_dict = get_floating_rates_floating_rate_id_response.from_dict(get_floating_rates_floating_rate_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


