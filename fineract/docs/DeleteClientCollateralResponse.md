# DeleteClientCollateralResponse

DeleteClientCollateralResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_client_collateral_response import DeleteClientCollateralResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteClientCollateralResponse from a JSON string
delete_client_collateral_response_instance = DeleteClientCollateralResponse.from_json(json)
# print the JSON string representation of the object
print DeleteClientCollateralResponse.to_json()

# convert the object into a dict
delete_client_collateral_response_dict = delete_client_collateral_response_instance.to_dict()
# create an instance of DeleteClientCollateralResponse from a dict
delete_client_collateral_response_form_dict = delete_client_collateral_response.from_dict(delete_client_collateral_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


