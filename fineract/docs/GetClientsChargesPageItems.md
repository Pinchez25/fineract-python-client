# GetClientsChargesPageItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**amount_outstanding** | **float** |  | [optional] 
**amount_paid** | **float** |  | [optional] 
**amount_waived** | **float** |  | [optional] 
**amount_written_off** | **float** |  | [optional] 
**charge_calculation_type** | [**GetClientChargeCalculationType**](GetClientChargeCalculationType.md) |  | [optional] 
**charge_id** | **int** |  | [optional] 
**charge_time_type** | [**GetClientChargeTimeType**](GetClientChargeTimeType.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**currency** | [**GetClientChargeCurrency**](GetClientChargeCurrency.md) |  | [optional] 
**due_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_paid** | **bool** |  | [optional] 
**is_waived** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_charges_page_items import GetClientsChargesPageItems

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsChargesPageItems from a JSON string
get_clients_charges_page_items_instance = GetClientsChargesPageItems.from_json(json)
# print the JSON string representation of the object
print GetClientsChargesPageItems.to_json()

# convert the object into a dict
get_clients_charges_page_items_dict = get_clients_charges_page_items_instance.to_dict()
# create an instance of GetClientsChargesPageItems from a dict
get_clients_charges_page_items_form_dict = get_clients_charges_page_items.from_dict(get_clients_charges_page_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


