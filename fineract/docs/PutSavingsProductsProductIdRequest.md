# PutSavingsProductsProductIdRequest

PutSavingsProductsProductIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_savings_products_product_id_request import PutSavingsProductsProductIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutSavingsProductsProductIdRequest from a JSON string
put_savings_products_product_id_request_instance = PutSavingsProductsProductIdRequest.from_json(json)
# print the JSON string representation of the object
print PutSavingsProductsProductIdRequest.to_json()

# convert the object into a dict
put_savings_products_product_id_request_dict = put_savings_products_product_id_request_instance.to_dict()
# create an instance of PutSavingsProductsProductIdRequest from a dict
put_savings_products_product_id_request_form_dict = put_savings_products_product_id_request.from_dict(put_savings_products_product_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


