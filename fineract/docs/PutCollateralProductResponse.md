# PutCollateralProductResponse

PutCollateralProductResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutCollateralProductRequest**](PutCollateralProductRequest.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_collateral_product_response import PutCollateralProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutCollateralProductResponse from a JSON string
put_collateral_product_response_instance = PutCollateralProductResponse.from_json(json)
# print the JSON string representation of the object
print PutCollateralProductResponse.to_json()

# convert the object into a dict
put_collateral_product_response_dict = put_collateral_product_response_instance.to_dict()
# create an instance of PutCollateralProductResponse from a dict
put_collateral_product_response_form_dict = put_collateral_product_response.from_dict(put_collateral_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


