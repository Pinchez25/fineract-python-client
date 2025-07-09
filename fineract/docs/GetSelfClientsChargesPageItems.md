# GetSelfClientsChargesPageItems


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
from fineract_client.models.get_self_clients_charges_page_items import GetSelfClientsChargesPageItems

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfClientsChargesPageItems from a JSON string
get_self_clients_charges_page_items_instance = GetSelfClientsChargesPageItems.from_json(json)
# print the JSON string representation of the object
print(GetSelfClientsChargesPageItems.to_json())

# convert the object into a dict
get_self_clients_charges_page_items_dict = get_self_clients_charges_page_items_instance.to_dict()
# create an instance of GetSelfClientsChargesPageItems from a dict
get_self_clients_charges_page_items_from_dict = GetSelfClientsChargesPageItems.from_dict(get_self_clients_charges_page_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


