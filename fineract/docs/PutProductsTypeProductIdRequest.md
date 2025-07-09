# PutProductsTypeProductIdRequest

PutProductsTypeProductIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**unit_price** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.put_products_type_product_id_request import PutProductsTypeProductIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutProductsTypeProductIdRequest from a JSON string
put_products_type_product_id_request_instance = PutProductsTypeProductIdRequest.from_json(json)
# print the JSON string representation of the object
print PutProductsTypeProductIdRequest.to_json()

# convert the object into a dict
put_products_type_product_id_request_dict = put_products_type_product_id_request_instance.to_dict()
# create an instance of PutProductsTypeProductIdRequest from a dict
put_products_type_product_id_request_form_dict = put_products_type_product_id_request.from_dict(put_products_type_product_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


