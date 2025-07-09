# PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest

PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**date_format** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request import PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest from a JSON string
put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request_instance = PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest.from_json(json)
# print the JSON string representation of the object
print PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest.to_json()

# convert the object into a dict
put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request_dict = put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request_instance.to_dict()
# create an instance of PutSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdRequest from a dict
put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request_form_dict = put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request.from_dict(put_savings_accounts_savings_account_id_charges_savings_account_charge_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


