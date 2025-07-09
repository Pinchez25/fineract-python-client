# PostProductsMarketPricePeriods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**from_date** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**share_value** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_products_market_price_periods import PostProductsMarketPricePeriods

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsMarketPricePeriods from a JSON string
post_products_market_price_periods_instance = PostProductsMarketPricePeriods.from_json(json)
# print the JSON string representation of the object
print PostProductsMarketPricePeriods.to_json()

# convert the object into a dict
post_products_market_price_periods_dict = post_products_market_price_periods_instance.to_dict()
# create an instance of PostProductsMarketPricePeriods from a dict
post_products_market_price_periods_form_dict = post_products_market_price_periods.from_dict(post_products_market_price_periods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


