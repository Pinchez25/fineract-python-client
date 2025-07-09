# PutTellersTellerIdCashiersCashierIdResponse

PutTellersTellerIdCashiersCashierIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutTellersTellerIdCashiersCashierIdResponseChanges**](PutTellersTellerIdCashiersCashierIdResponseChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 
**sub_resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_tellers_teller_id_cashiers_cashier_id_response import PutTellersTellerIdCashiersCashierIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutTellersTellerIdCashiersCashierIdResponse from a JSON string
put_tellers_teller_id_cashiers_cashier_id_response_instance = PutTellersTellerIdCashiersCashierIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutTellersTellerIdCashiersCashierIdResponse.to_json())

# convert the object into a dict
put_tellers_teller_id_cashiers_cashier_id_response_dict = put_tellers_teller_id_cashiers_cashier_id_response_instance.to_dict()
# create an instance of PutTellersTellerIdCashiersCashierIdResponse from a dict
put_tellers_teller_id_cashiers_cashier_id_response_from_dict = PutTellersTellerIdCashiersCashierIdResponse.from_dict(put_tellers_teller_id_cashiers_cashier_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


