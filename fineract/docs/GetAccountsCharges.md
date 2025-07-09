# GetAccountsCharges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**amount_or_percentage** | **float** |  | [optional] 
**amount_outstanding** | **float** |  | [optional] 
**amount_paid** | **float** |  | [optional] 
**amount_percentage_applied_to** | **float** |  | [optional] 
**amount_waived** | **float** |  | [optional] 
**amount_written_off** | **float** |  | [optional] 
**charge_calculation_type** | [**GetAccountsChargeCalculationType**](GetAccountsChargeCalculationType.md) |  | [optional] 
**charge_id** | **int** |  | [optional] 
**charge_time_type** | [**GetAccountsChargeTimeType**](GetAccountsChargeTimeType.md) |  | [optional] 
**currency** | [**GetAccountsChargesCurrency**](GetAccountsChargesCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**percentage** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_charges import GetAccountsCharges

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsCharges from a JSON string
get_accounts_charges_instance = GetAccountsCharges.from_json(json)
# print the JSON string representation of the object
print GetAccountsCharges.to_json()

# convert the object into a dict
get_accounts_charges_dict = get_accounts_charges_instance.to_dict()
# create an instance of GetAccountsCharges from a dict
get_accounts_charges_form_dict = get_accounts_charges.from_dict(get_accounts_charges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


