# GetChargesAppliesToResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_charges_applies_to_response import GetChargesAppliesToResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargesAppliesToResponse from a JSON string
get_charges_applies_to_response_instance = GetChargesAppliesToResponse.from_json(json)
# print the JSON string representation of the object
print(GetChargesAppliesToResponse.to_json())

# convert the object into a dict
get_charges_applies_to_response_dict = get_charges_applies_to_response_instance.to_dict()
# create an instance of GetChargesAppliesToResponse from a dict
get_charges_applies_to_response_from_dict = GetChargesAppliesToResponse.from_dict(get_charges_applies_to_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


