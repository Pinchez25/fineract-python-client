# GetProductsEquityAccountOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** |  | [optional] 
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**manual_entries_allowed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**name_decorated** | **str** |  | [optional] 
**tag_id** | [**GetProductsTagId**](GetProductsTagId.md) |  | [optional] 
**type** | [**GetEquityType**](GetEquityType.md) |  | [optional] 
**usage** | [**GetProductsLiabilityUsage**](GetProductsLiabilityUsage.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_products_equity_account_options import GetProductsEquityAccountOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsEquityAccountOptions from a JSON string
get_products_equity_account_options_instance = GetProductsEquityAccountOptions.from_json(json)
# print the JSON string representation of the object
print(GetProductsEquityAccountOptions.to_json())

# convert the object into a dict
get_products_equity_account_options_dict = get_products_equity_account_options_instance.to_dict()
# create an instance of GetProductsEquityAccountOptions from a dict
get_products_equity_account_options_from_dict = GetProductsEquityAccountOptions.from_dict(get_products_equity_account_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


