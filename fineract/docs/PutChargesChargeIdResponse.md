# PutChargesChargeIdResponse

PutChargesChargeIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutChargesChargeIdRequest**](PutChargesChargeIdRequest.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_charges_charge_id_response import PutChargesChargeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutChargesChargeIdResponse from a JSON string
put_charges_charge_id_response_instance = PutChargesChargeIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutChargesChargeIdResponse.to_json())

# convert the object into a dict
put_charges_charge_id_response_dict = put_charges_charge_id_response_instance.to_dict()
# create an instance of PutChargesChargeIdResponse from a dict
put_charges_charge_id_response_from_dict = PutChargesChargeIdResponse.from_dict(put_charges_charge_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


