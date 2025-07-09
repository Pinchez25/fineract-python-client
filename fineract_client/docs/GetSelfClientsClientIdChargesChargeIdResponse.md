# GetSelfClientsClientIdChargesChargeIdResponse

GetSelfClientsClientIdChargesChargeIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**amount_outstanding** | **float** |  | [optional] 
**amount_paid** | **float** |  | [optional] 
**amount_waived** | **float** |  | [optional] 
**amount_written_off** | **float** |  | [optional] 
**charge_calculation_type** | [**GetSelfClientsChargeCalculationType**](GetSelfClientsChargeCalculationType.md) |  | [optional] 
**charge_id** | **int** |  | [optional] 
**charge_time_type** | [**GetSelfClientsChargeTimeType**](GetSelfClientsChargeTimeType.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**currency** | [**GetSelfClientsSavingsAccountsCurrency**](GetSelfClientsSavingsAccountsCurrency.md) |  | [optional] 
**due_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_paid** | **bool** |  | [optional] 
**is_waived** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_clients_client_id_charges_charge_id_response import GetSelfClientsClientIdChargesChargeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsClientIdChargesChargeIdResponse from a JSON string
get_self_clients_client_id_charges_charge_id_response_instance = GetSelfClientsClientIdChargesChargeIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetSelfClientsClientIdChargesChargeIdResponse.to_json())

# convert the object into a dict
get_self_clients_client_id_charges_charge_id_response_dict = get_self_clients_client_id_charges_charge_id_response_instance.to_dict()
# create an instance of GetSelfClientsClientIdChargesChargeIdResponse from a dict
get_self_clients_client_id_charges_charge_id_response_from_dict = GetSelfClientsClientIdChargesChargeIdResponse.from_dict(get_self_clients_client_id_charges_charge_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


