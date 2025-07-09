# PutProductsTypeProductIdResponse

PutProductsTypeProductIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutProductsChanges**](PutProductsChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_products_type_product_id_response import PutProductsTypeProductIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutProductsTypeProductIdResponse from a JSON string
put_products_type_product_id_response_instance = PutProductsTypeProductIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutProductsTypeProductIdResponse.to_json())

# convert the object into a dict
put_products_type_product_id_response_dict = put_products_type_product_id_response_instance.to_dict()
# create an instance of PutProductsTypeProductIdResponse from a dict
put_products_type_product_id_response_from_dict = PutProductsTypeProductIdResponse.from_dict(put_products_type_product_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


