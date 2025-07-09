# PutFixedDepositProductsProductIdRequest

PutFixedDepositProductsProductIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**min_deposit_term** | **int** |  | [optional] 
**min_deposit_term_type_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_fixed_deposit_products_product_id_request import PutFixedDepositProductsProductIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutFixedDepositProductsProductIdRequest from a JSON string
put_fixed_deposit_products_product_id_request_instance = PutFixedDepositProductsProductIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutFixedDepositProductsProductIdRequest.to_json())

# convert the object into a dict
put_fixed_deposit_products_product_id_request_dict = put_fixed_deposit_products_product_id_request_instance.to_dict()
# create an instance of PutFixedDepositProductsProductIdRequest from a dict
put_fixed_deposit_products_product_id_request_from_dict = PutFixedDepositProductsProductIdRequest.from_dict(put_fixed_deposit_products_product_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


