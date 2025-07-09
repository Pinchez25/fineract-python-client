# GetSelfSavingsAccountsAccountIdChargesResponse

GetSelfSavingsAccountsAccountIdChargesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**amount** | **int** |  | [optional] 
**amount_or_percentage** | **int** |  | [optional] 
**amount_outstanding** | **int** |  | [optional] 
**amount_paid** | **int** |  | [optional] 
**amount_percentage_applied_to** | **float** |  | [optional] 
**amount_waived** | **int** |  | [optional] 
**amount_written_off** | **int** |  | [optional] 
**charge_calculation_type** | [**GetSelfSavingsChargeCalculationType**](GetSelfSavingsChargeCalculationType.md) |  | [optional] 
**charge_id** | **int** |  | [optional] 
**charge_time_type** | [**GetSelfSavingsChargeTimeType**](GetSelfSavingsChargeTimeType.md) |  | [optional] 
**currency** | [**GetSelfSavingsCurrency**](GetSelfSavingsCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_savings_accounts_account_id_charges_response import GetSelfSavingsAccountsAccountIdChargesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfSavingsAccountsAccountIdChargesResponse from a JSON string
get_self_savings_accounts_account_id_charges_response_instance = GetSelfSavingsAccountsAccountIdChargesResponse.from_json(json)
# print the JSON string representation of the object
print GetSelfSavingsAccountsAccountIdChargesResponse.to_json()

# convert the object into a dict
get_self_savings_accounts_account_id_charges_response_dict = get_self_savings_accounts_account_id_charges_response_instance.to_dict()
# create an instance of GetSelfSavingsAccountsAccountIdChargesResponse from a dict
get_self_savings_accounts_account_id_charges_response_form_dict = get_self_savings_accounts_account_id_charges_response.from_dict(get_self_savings_accounts_account_id_charges_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


