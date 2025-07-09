# PutClientCollateralRequest

PutClientCollateralRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.put_client_collateral_request import PutClientCollateralRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutClientCollateralRequest from a JSON string
put_client_collateral_request_instance = PutClientCollateralRequest.from_json(json)
# print the JSON string representation of the object
print(PutClientCollateralRequest.to_json())

# convert the object into a dict
put_client_collateral_request_dict = put_client_collateral_request_instance.to_dict()
# create an instance of PutClientCollateralRequest from a dict
put_client_collateral_request_from_dict = PutClientCollateralRequest.from_dict(put_client_collateral_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


