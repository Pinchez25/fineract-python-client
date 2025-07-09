# GetChargesCalculationTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_charges_calculation_type_response import GetChargesCalculationTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargesCalculationTypeResponse from a JSON string
get_charges_calculation_type_response_instance = GetChargesCalculationTypeResponse.from_json(json)
# print the JSON string representation of the object
print(GetChargesCalculationTypeResponse.to_json())

# convert the object into a dict
get_charges_calculation_type_response_dict = get_charges_calculation_type_response_instance.to_dict()
# create an instance of GetChargesCalculationTypeResponse from a dict
get_charges_calculation_type_response_from_dict = GetChargesCalculationTypeResponse.from_dict(get_charges_calculation_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


