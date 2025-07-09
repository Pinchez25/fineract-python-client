# GetTellersTellerIdCashiersCashierIdResponse

GetTellersTellerIdCashiersCashierIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**end_date** | **date** |  | [optional] 
**end_time** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_full_day** | **bool** |  | [optional] 
**staff_id** | **int** |  | [optional] 
**staff_name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**start_time** | **str** |  | [optional] 
**teller_id** | **int** |  | [optional] 
**teller_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_tellers_teller_id_cashiers_cashier_id_response import GetTellersTellerIdCashiersCashierIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTellersTellerIdCashiersCashierIdResponse from a JSON string
get_tellers_teller_id_cashiers_cashier_id_response_instance = GetTellersTellerIdCashiersCashierIdResponse.from_json(json)
# print the JSON string representation of the object
print GetTellersTellerIdCashiersCashierIdResponse.to_json()

# convert the object into a dict
get_tellers_teller_id_cashiers_cashier_id_response_dict = get_tellers_teller_id_cashiers_cashier_id_response_instance.to_dict()
# create an instance of GetTellersTellerIdCashiersCashierIdResponse from a dict
get_tellers_teller_id_cashiers_cashier_id_response_form_dict = get_tellers_teller_id_cashiers_cashier_id_response.from_dict(get_tellers_teller_id_cashiers_cashier_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


