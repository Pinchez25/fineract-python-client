# PutChargeTransactionChangesResponse

PutChargeTransactionChangesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutChargeTransactionChangesResponseChanges**](PutChargeTransactionChangesResponseChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_external_id** | **str** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**sub_resource_external_id** | **str** |  | [optional] 
**sub_resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_charge_transaction_changes_response import PutChargeTransactionChangesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutChargeTransactionChangesResponse from a JSON string
put_charge_transaction_changes_response_instance = PutChargeTransactionChangesResponse.from_json(json)
# print the JSON string representation of the object
print(PutChargeTransactionChangesResponse.to_json())

# convert the object into a dict
put_charge_transaction_changes_response_dict = put_charge_transaction_changes_response_instance.to_dict()
# create an instance of PutChargeTransactionChangesResponse from a dict
put_charge_transaction_changes_response_from_dict = PutChargeTransactionChangesResponse.from_dict(put_charge_transaction_changes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


