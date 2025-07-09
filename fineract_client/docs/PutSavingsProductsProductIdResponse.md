# PutSavingsProductsProductIdResponse

PutSavingsProductsProductIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutSavingsChanges**](PutSavingsChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_savings_products_product_id_response import PutSavingsProductsProductIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutSavingsProductsProductIdResponse from a JSON string
put_savings_products_product_id_response_instance = PutSavingsProductsProductIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutSavingsProductsProductIdResponse.to_json())

# convert the object into a dict
put_savings_products_product_id_response_dict = put_savings_products_product_id_response_instance.to_dict()
# create an instance of PutSavingsProductsProductIdResponse from a dict
put_savings_products_product_id_response_from_dict = PutSavingsProductsProductIdResponse.from_dict(put_savings_products_product_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


