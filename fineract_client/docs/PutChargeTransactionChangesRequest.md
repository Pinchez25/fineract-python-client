# PutChargeTransactionChangesRequest

PutChargeTransactionChangesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_charge_transaction_changes_request import PutChargeTransactionChangesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutChargeTransactionChangesRequest from a JSON string
put_charge_transaction_changes_request_instance = PutChargeTransactionChangesRequest.from_json(json)
# print the JSON string representation of the object
print(PutChargeTransactionChangesRequest.to_json())

# convert the object into a dict
put_charge_transaction_changes_request_dict = put_charge_transaction_changes_request_instance.to_dict()
# create an instance of PutChargeTransactionChangesRequest from a dict
put_charge_transaction_changes_request_from_dict = PutChargeTransactionChangesRequest.from_dict(put_charge_transaction_changes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


