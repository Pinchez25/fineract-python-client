# PostFixedDepositProductsRequest

PostFixedDepositProductsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_rule** | **int** |  | [optional] 
**charts** | [**List[PostFixedDepositProductsCharts]**](PostFixedDepositProductsCharts.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**digits_after_decimal** | **int** |  | [optional] 
**in_multiples_of** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | **int** |  | [optional] 
**interest_calculation_type** | **int** |  | [optional] 
**interest_compounding_period_type** | **int** |  | [optional] 
**interest_posting_period_type** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**max_deposit_term** | **int** |  | [optional] 
**max_deposit_term_type_id** | **int** |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 
**min_deposit_term_type_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**pre_closure_penal_applicable** | **bool** |  | [optional] 
**pre_closure_penal_interest** | **float** |  | [optional] 
**pre_closure_penal_interest_on_type_id** | **int** |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_fixed_deposit_products_request import PostFixedDepositProductsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFixedDepositProductsRequest from a JSON string
post_fixed_deposit_products_request_instance = PostFixedDepositProductsRequest.from_json(json)
# print the JSON string representation of the object
print(PostFixedDepositProductsRequest.to_json())

# convert the object into a dict
post_fixed_deposit_products_request_dict = post_fixed_deposit_products_request_instance.to_dict()
# create an instance of PostFixedDepositProductsRequest from a dict
post_fixed_deposit_products_request_from_dict = PostFixedDepositProductsRequest.from_dict(post_fixed_deposit_products_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


