# PutTellersTellerIdCashiersCashierIdRequest

PutTellersTellerIdCashiersCashierIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**end_date** | **date** |  | [optional] 
**is_full_day** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**staff_id** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.put_tellers_teller_id_cashiers_cashier_id_request import PutTellersTellerIdCashiersCashierIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutTellersTellerIdCashiersCashierIdRequest from a JSON string
put_tellers_teller_id_cashiers_cashier_id_request_instance = PutTellersTellerIdCashiersCashierIdRequest.from_json(json)
# print the JSON string representation of the object
print PutTellersTellerIdCashiersCashierIdRequest.to_json()

# convert the object into a dict
put_tellers_teller_id_cashiers_cashier_id_request_dict = put_tellers_teller_id_cashiers_cashier_id_request_instance.to_dict()
# create an instance of PutTellersTellerIdCashiersCashierIdRequest from a dict
put_tellers_teller_id_cashiers_cashier_id_request_form_dict = put_tellers_teller_id_cashiers_cashier_id_request.from_dict(put_tellers_teller_id_cashiers_cashier_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


