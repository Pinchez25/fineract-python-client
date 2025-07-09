# GetProductsMarketPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**share_value** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_products_market_price import GetProductsMarketPrice

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsMarketPrice from a JSON string
get_products_market_price_instance = GetProductsMarketPrice.from_json(json)
# print the JSON string representation of the object
print(GetProductsMarketPrice.to_json())

# convert the object into a dict
get_products_market_price_dict = get_products_market_price_instance.to_dict()
# create an instance of GetProductsMarketPrice from a dict
get_products_market_price_from_dict = GetProductsMarketPrice.from_dict(get_products_market_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


