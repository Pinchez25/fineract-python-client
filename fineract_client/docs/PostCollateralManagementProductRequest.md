# PostCollateralManagementProductRequest

PostCollateralManagementProductRequest

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
from fineract_client.models.post_collateral_management_product_request import PostCollateralManagementProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCollateralManagementProductRequest from a JSON string
post_collateral_management_product_request_instance = PostCollateralManagementProductRequest.from_json(json)
# print the JSON string representation of the object
print(PostCollateralManagementProductRequest.to_json())

# convert the object into a dict
post_collateral_management_product_request_dict = post_collateral_management_product_request_instance.to_dict()
# create an instance of PostCollateralManagementProductRequest from a dict
post_collateral_management_product_request_from_dict = PostCollateralManagementProductRequest.from_dict(post_collateral_management_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


