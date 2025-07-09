# PutFloatingRatesFloatingRateIdResponse

PutFloatingRatesFloatingRateIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutFloatingRatesChanges**](PutFloatingRatesChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_floating_rates_floating_rate_id_response import PutFloatingRatesFloatingRateIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutFloatingRatesFloatingRateIdResponse from a JSON string
put_floating_rates_floating_rate_id_response_instance = PutFloatingRatesFloatingRateIdResponse.from_json(json)
# print the JSON string representation of the object
print PutFloatingRatesFloatingRateIdResponse.to_json()

# convert the object into a dict
put_floating_rates_floating_rate_id_response_dict = put_floating_rates_floating_rate_id_response_instance.to_dict()
# create an instance of PutFloatingRatesFloatingRateIdResponse from a dict
put_floating_rates_floating_rate_id_response_form_dict = put_floating_rates_floating_rate_id_response.from_dict(put_floating_rates_floating_rate_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


