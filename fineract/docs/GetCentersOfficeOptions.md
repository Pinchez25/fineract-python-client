# GetCentersOfficeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_office_options import GetCentersOfficeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersOfficeOptions from a JSON string
get_centers_office_options_instance = GetCentersOfficeOptions.from_json(json)
# print the JSON string representation of the object
print(GetCentersOfficeOptions.to_json())

# convert the object into a dict
get_centers_office_options_dict = get_centers_office_options_instance.to_dict()
# create an instance of GetCentersOfficeOptions from a dict
get_centers_office_options_from_dict = GetCentersOfficeOptions.from_dict(get_centers_office_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


