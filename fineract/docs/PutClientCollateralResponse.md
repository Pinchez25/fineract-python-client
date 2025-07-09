# PutClientCollateralResponse

PutClientCollateralResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutClientCollateralRequest**](PutClientCollateralRequest.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_client_collateral_response import PutClientCollateralResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutClientCollateralResponse from a JSON string
put_client_collateral_response_instance = PutClientCollateralResponse.from_json(json)
# print the JSON string representation of the object
print PutClientCollateralResponse.to_json()

# convert the object into a dict
put_client_collateral_response_dict = put_client_collateral_response_instance.to_dict()
# create an instance of PutClientCollateralResponse from a dict
put_client_collateral_response_form_dict = put_client_collateral_response.from_dict(put_client_collateral_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


