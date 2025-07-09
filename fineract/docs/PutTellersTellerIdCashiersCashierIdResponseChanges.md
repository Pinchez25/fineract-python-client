# PutTellersTellerIdCashiersCashierIdResponseChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**end_date** | **date** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_tellers_teller_id_cashiers_cashier_id_response_changes import PutTellersTellerIdCashiersCashierIdResponseChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutTellersTellerIdCashiersCashierIdResponseChanges from a JSON string
put_tellers_teller_id_cashiers_cashier_id_response_changes_instance = PutTellersTellerIdCashiersCashierIdResponseChanges.from_json(json)
# print the JSON string representation of the object
print(PutTellersTellerIdCashiersCashierIdResponseChanges.to_json())

# convert the object into a dict
put_tellers_teller_id_cashiers_cashier_id_response_changes_dict = put_tellers_teller_id_cashiers_cashier_id_response_changes_instance.to_dict()
# create an instance of PutTellersTellerIdCashiersCashierIdResponseChanges from a dict
put_tellers_teller_id_cashiers_cashier_id_response_changes_from_dict = PutTellersTellerIdCashiersCashierIdResponseChanges.from_dict(put_tellers_teller_id_cashiers_cashier_id_response_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


