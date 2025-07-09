# PutLoanProductsProductIdResponse

PutLoanProductsProductIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutLoanChanges**](PutLoanChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_loan_products_product_id_response import PutLoanProductsProductIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutLoanProductsProductIdResponse from a JSON string
put_loan_products_product_id_response_instance = PutLoanProductsProductIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutLoanProductsProductIdResponse.to_json())

# convert the object into a dict
put_loan_products_product_id_response_dict = put_loan_products_product_id_response_instance.to_dict()
# create an instance of PutLoanProductsProductIdResponse from a dict
put_loan_products_product_id_response_from_dict = PutLoanProductsProductIdResponse.from_dict(put_loan_products_product_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


