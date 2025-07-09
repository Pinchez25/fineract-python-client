# PostProductsTypeRequest

PostProductsTypeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_rule** | **int** |  | [optional] 
**allow_dividend_calculation_for_inactive_clients** | **bool** |  | [optional] 
**charges_selected** | [**List[PostProductsChargesSelected]**](PostProductsChargesSelected.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**digits_after_decimal** | **int** |  | [optional] 
**in_multiples_of** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**lockin_period_frequency** | **int** |  | [optional] 
**lockin_period_frequency_type** | **int** |  | [optional] 
**market_price_periods** | [**List[PostProductsMarketPricePeriods]**](PostProductsMarketPricePeriods.md) |  | [optional] 
**maximum_shares** | **int** |  | [optional] 
**minimum_active_period_for_dividends** | **int** |  | [optional] 
**minimum_shares** | **int** |  | [optional] 
**minimumactiveperiod_frequency_type** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**nominal_shares** | **int** |  | [optional] 
**shares_issued** | **int** |  | [optional] 
**short_name** | **str** |  | [optional] 
**total_shares** | **int** |  | [optional] 
**unit_price** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_products_type_request import PostProductsTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsTypeRequest from a JSON string
post_products_type_request_instance = PostProductsTypeRequest.from_json(json)
# print the JSON string representation of the object
print(PostProductsTypeRequest.to_json())

# convert the object into a dict
post_products_type_request_dict = post_products_type_request_instance.to_dict()
# create an instance of PostProductsTypeRequest from a dict
post_products_type_request_from_dict = PostProductsTypeRequest.from_dict(post_products_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


