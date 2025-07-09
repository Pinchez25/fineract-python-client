# PostClientCollateralRequest

PostClientCollateralRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.post_client_collateral_request import PostClientCollateralRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientCollateralRequest from a JSON string
post_client_collateral_request_instance = PostClientCollateralRequest.from_json(json)
# print the JSON string representation of the object
print(PostClientCollateralRequest.to_json())

# convert the object into a dict
post_client_collateral_request_dict = post_client_collateral_request_instance.to_dict()
# create an instance of PostClientCollateralRequest from a dict
post_client_collateral_request_from_dict = PostClientCollateralRequest.from_dict(post_client_collateral_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


