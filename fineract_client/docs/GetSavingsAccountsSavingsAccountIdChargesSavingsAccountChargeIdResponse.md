# GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse

GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**amount_or_percentage** | **float** |  | [optional] 
**amount_outstanding** | **float** |  | [optional] 
**amount_paid** | **float** |  | [optional] 
**amount_percentage_applied_to** | **float** |  | [optional] 
**amount_waived** | **float** |  | [optional] 
**amount_written_off** | **float** |  | [optional] 
**charge_calculation_type** | [**GetChargesChargeCalculationType**](GetChargesChargeCalculationType.md) |  | [optional] 
**charge_id** | **int** |  | [optional] 
**charge_time_type** | [**GetChargesChargeTimeType**](GetChargesChargeTimeType.md) |  | [optional] 
**currency** | [**GetChargesCurrencyResponse**](GetChargesCurrencyResponse.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_accounts_savings_account_id_charges_savings_account_charge_id_response import GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse from a JSON string
get_savings_accounts_savings_account_id_charges_savings_account_charge_id_response_instance = GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse.to_json())

# convert the object into a dict
get_savings_accounts_savings_account_id_charges_savings_account_charge_id_response_dict = get_savings_accounts_savings_account_id_charges_savings_account_charge_id_response_instance.to_dict()
# create an instance of GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse from a dict
get_savings_accounts_savings_account_id_charges_savings_account_charge_id_response_from_dict = GetSavingsAccountsSavingsAccountIdChargesSavingsAccountChargeIdResponse.from_dict(get_savings_accounts_savings_account_id_charges_savings_account_charge_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


