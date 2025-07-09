# GetCollateralProductTemplate

GetCollateralProductTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**GetCurrencyData**](GetCurrencyData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_collateral_product_template import GetCollateralProductTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of GetCollateralProductTemplate from a JSON string
get_collateral_product_template_instance = GetCollateralProductTemplate.from_json(json)
# print the JSON string representation of the object
print(GetCollateralProductTemplate.to_json())

# convert the object into a dict
get_collateral_product_template_dict = get_collateral_product_template_instance.to_dict()
# create an instance of GetCollateralProductTemplate from a dict
get_collateral_product_template_from_dict = GetCollateralProductTemplate.from_dict(get_collateral_product_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


