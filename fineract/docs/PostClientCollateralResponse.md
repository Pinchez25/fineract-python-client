# PostClientCollateralResponse

PostClientCollateralResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_client_collateral_response import PostClientCollateralResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostClientCollateralResponse from a JSON string
post_client_collateral_response_instance = PostClientCollateralResponse.from_json(json)
# print the JSON string representation of the object
print PostClientCollateralResponse.to_json()

# convert the object into a dict
post_client_collateral_response_dict = post_client_collateral_response_instance.to_dict()
# create an instance of PostClientCollateralResponse from a dict
post_client_collateral_response_form_dict = post_client_collateral_response.from_dict(post_client_collateral_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


