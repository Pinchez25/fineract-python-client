# GetAssetType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_asset_type import GetAssetType

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetType from a JSON string
get_asset_type_instance = GetAssetType.from_json(json)
# print the JSON string representation of the object
print(GetAssetType.to_json())

# convert the object into a dict
get_asset_type_dict = get_asset_type_instance.to_dict()
# create an instance of GetAssetType from a dict
get_asset_type_from_dict = GetAssetType.from_dict(get_asset_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


