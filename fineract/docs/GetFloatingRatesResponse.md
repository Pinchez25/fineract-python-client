# GetFloatingRatesResponse

GetFloatingRatesResponse

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

## Example

```python
from fineract_client.models.get_floating_rates_response import GetFloatingRatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFloatingRatesResponse from a JSON string
get_floating_rates_response_instance = GetFloatingRatesResponse.from_json(json)
# print the JSON string representation of the object
print GetFloatingRatesResponse.to_json()

# convert the object into a dict
get_floating_rates_response_dict = get_floating_rates_response_instance.to_dict()
# create an instance of GetFloatingRatesResponse from a dict
get_floating_rates_response_form_dict = get_floating_rates_response.from_dict(get_floating_rates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


