# GetCollateralManagementsResponse

GetCollateralManagementsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_price** | **float** |  | [optional] 
**currency** | [**GetCollateralCurrencyResponse**](GetCollateralCurrencyResponse.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**pct_to_base** | **float** |  | [optional] 
**unit_type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_collateral_managements_response import GetCollateralManagementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCollateralManagementsResponse from a JSON string
get_collateral_managements_response_instance = GetCollateralManagementsResponse.from_json(json)
# print the JSON string representation of the object
print GetCollateralManagementsResponse.to_json()

# convert the object into a dict
get_collateral_managements_response_dict = get_collateral_managements_response_instance.to_dict()
# create an instance of GetCollateralManagementsResponse from a dict
get_collateral_managements_response_form_dict = get_collateral_managements_response.from_dict(get_collateral_managements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


