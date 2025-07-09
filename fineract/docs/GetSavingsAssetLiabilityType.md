# GetSavingsAssetLiabilityType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_asset_liability_type import GetSavingsAssetLiabilityType

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsAssetLiabilityType from a JSON string
get_savings_asset_liability_type_instance = GetSavingsAssetLiabilityType.from_json(json)
# print the JSON string representation of the object
print GetSavingsAssetLiabilityType.to_json()

# convert the object into a dict
get_savings_asset_liability_type_dict = get_savings_asset_liability_type_instance.to_dict()
# create an instance of GetSavingsAssetLiabilityType from a dict
get_savings_asset_liability_type_form_dict = get_savings_asset_liability_type.from_dict(get_savings_asset_liability_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


