# PostSavingsProductsRequest

PostSavingsProductsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_mapping_for_payment** | **str** |  | [optional] 
**accounting_rule** | **int** |  | [optional] 
**charges** | [**List[PostSavingsCharges]**](PostSavingsCharges.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**digits_after_decimal** | **int** |  | [optional] 
**in_multiples_of** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | **int** |  | [optional] 
**interest_calculation_type** | **int** |  | [optional] 
**interest_compounding_period_type** | **int** |  | [optional] 
**interest_posting_period_type** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nominal_annual_interest_rate** | **float** |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_savings_products_request import PostSavingsProductsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSavingsProductsRequest from a JSON string
post_savings_products_request_instance = PostSavingsProductsRequest.from_json(json)
# print the JSON string representation of the object
print(PostSavingsProductsRequest.to_json())

# convert the object into a dict
post_savings_products_request_dict = post_savings_products_request_instance.to_dict()
# create an instance of PostSavingsProductsRequest from a dict
post_savings_products_request_from_dict = PostSavingsProductsRequest.from_dict(post_savings_products_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


