# PutCollateralProductRequest

PutCollateralProductRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_price** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**pct_to_base** | **float** |  | [optional] 
**quality** | **str** |  | [optional] 
**unit_type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_collateral_product_request import PutCollateralProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutCollateralProductRequest from a JSON string
put_collateral_product_request_instance = PutCollateralProductRequest.from_json(json)
# print the JSON string representation of the object
print PutCollateralProductRequest.to_json()

# convert the object into a dict
put_collateral_product_request_dict = put_collateral_product_request_instance.to_dict()
# create an instance of PutCollateralProductRequest from a dict
put_collateral_product_request_form_dict = put_collateral_product_request.from_dict(put_collateral_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


