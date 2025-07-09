# PutChargeTransactionChangesResponseChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**var_date** | **date** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fee_charges_portion** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_portion** | **float** |  | [optional] 
**outstanding_loan_balance** | **float** |  | [optional] 
**penalty_charges_portion** | **float** |  | [optional] 
**principal_portion** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.put_charge_transaction_changes_response_changes import PutChargeTransactionChangesResponseChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutChargeTransactionChangesResponseChanges from a JSON string
put_charge_transaction_changes_response_changes_instance = PutChargeTransactionChangesResponseChanges.from_json(json)
# print the JSON string representation of the object
print(PutChargeTransactionChangesResponseChanges.to_json())

# convert the object into a dict
put_charge_transaction_changes_response_changes_dict = put_charge_transaction_changes_response_changes_instance.to_dict()
# create an instance of PutChargeTransactionChangesResponseChanges from a dict
put_charge_transaction_changes_response_changes_from_dict = PutChargeTransactionChangesResponseChanges.from_dict(put_charge_transaction_changes_response_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


