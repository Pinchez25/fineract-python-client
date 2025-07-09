# PutFixedDepositProductsProductIdResponse

PutFixedDepositProductsProductIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutFixedDepositProductsChanges**](PutFixedDepositProductsChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_fixed_deposit_products_product_id_response import PutFixedDepositProductsProductIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutFixedDepositProductsProductIdResponse from a JSON string
put_fixed_deposit_products_product_id_response_instance = PutFixedDepositProductsProductIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutFixedDepositProductsProductIdResponse.to_json())

# convert the object into a dict
put_fixed_deposit_products_product_id_response_dict = put_fixed_deposit_products_product_id_response_instance.to_dict()
# create an instance of PutFixedDepositProductsProductIdResponse from a dict
put_fixed_deposit_products_product_id_response_from_dict = PutFixedDepositProductsProductIdResponse.from_dict(put_fixed_deposit_products_product_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


