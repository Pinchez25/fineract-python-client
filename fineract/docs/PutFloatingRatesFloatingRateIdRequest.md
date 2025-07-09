# PutFloatingRatesFloatingRateIdRequest

PutFloatingRatesFloatingRateIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional] 
**is_base_lending_rate** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**rate_periods** | [**List[PostFloatingRatesRatePeriods]**](PostFloatingRatesRatePeriods.md) |  | [optional] 

## Example

```python
from fineract_client.models.put_floating_rates_floating_rate_id_request import PutFloatingRatesFloatingRateIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutFloatingRatesFloatingRateIdRequest from a JSON string
put_floating_rates_floating_rate_id_request_instance = PutFloatingRatesFloatingRateIdRequest.from_json(json)
# print the JSON string representation of the object
print PutFloatingRatesFloatingRateIdRequest.to_json()

# convert the object into a dict
put_floating_rates_floating_rate_id_request_dict = put_floating_rates_floating_rate_id_request_instance.to_dict()
# create an instance of PutFloatingRatesFloatingRateIdRequest from a dict
put_floating_rates_floating_rate_id_request_form_dict = put_floating_rates_floating_rate_id_request.from_dict(put_floating_rates_floating_rate_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


