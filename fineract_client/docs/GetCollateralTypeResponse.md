# GetCollateralTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_collateral_type_response import GetCollateralTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCollateralTypeResponse from a JSON string
get_collateral_type_response_instance = GetCollateralTypeResponse.from_json(json)
# print the JSON string representation of the object
print(GetCollateralTypeResponse.to_json())

# convert the object into a dict
get_collateral_type_response_dict = get_collateral_type_response_instance.to_dict()
# create an instance of GetCollateralTypeResponse from a dict
get_collateral_type_response_from_dict = GetCollateralTypeResponse.from_dict(get_collateral_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


