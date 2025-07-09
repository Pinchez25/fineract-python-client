# PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse

PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutSavingsChanges**](PutSavingsChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_savings_accounts_savings_account_id_charges_savings_account_charge_id_response import PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse from a JSON string
put_savings_accounts_savings_account_id_charges_savings_account_charge_id_response_instance = PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse.to_json())

# convert the object into a dict
put_savings_accounts_savings_account_id_charges_savings_account_charge_id_response_dict = put_savings_accounts_savings_account_id_charges_savings_account_charge_id_response_instance.to_dict()
# create an instance of PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse from a dict
put_savings_accounts_savings_account_id_charges_savings_account_charge_id_response_from_dict = PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse.from_dict(put_savings_accounts_savings_account_id_charges_savings_account_charge_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


