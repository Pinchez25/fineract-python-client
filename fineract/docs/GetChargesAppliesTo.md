# GetChargesAppliesTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_charges_applies_to import GetChargesAppliesTo

# TODO update the JSON string below
json = "{}"
# create an instance of GetChargesAppliesTo from a JSON string
get_charges_applies_to_instance = GetChargesAppliesTo.from_json(json)
# print the JSON string representation of the object
print(GetChargesAppliesTo.to_json())

# convert the object into a dict
get_charges_applies_to_dict = get_charges_applies_to_instance.to_dict()
# create an instance of GetChargesAppliesTo from a dict
get_charges_applies_to_from_dict = GetChargesAppliesTo.from_dict(get_charges_applies_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


