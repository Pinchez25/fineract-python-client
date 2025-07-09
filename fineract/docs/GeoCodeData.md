# GeoCodeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **str** |  | 
**longitude** | **str** |  | 

## Example

```python
from fineract_client.models.geo_code_data import GeoCodeData

# TODO update the JSON string below
json = "{}"
# create an instance of GeoCodeData from a JSON string
geo_code_data_instance = GeoCodeData.from_json(json)
# print the JSON string representation of the object
print(GeoCodeData.to_json())

# convert the object into a dict
geo_code_data_dict = geo_code_data_instance.to_dict()
# create an instance of GeoCodeData from a dict
geo_code_data_from_dict = GeoCodeData.from_dict(geo_code_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


