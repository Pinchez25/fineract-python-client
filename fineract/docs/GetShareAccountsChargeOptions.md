# GetShareAccountsChargeOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**amount** | **int** |  | [optional] 
**calculation_type** | [**GetShareAccountsChargeCalculationType**](GetShareAccountsChargeCalculationType.md) |  | [optional] 
**charge_applies_to** | [**GetShareAccountsChargeAppliesTo**](GetShareAccountsChargeAppliesTo.md) |  | [optional] 
**charge_time_type** | [**GetShareAccountsChargeTimeType**](GetShareAccountsChargeTimeType.md) |  | [optional] 
**currency** | [**GetShareAccountsCurrency**](GetShareAccountsCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**payment_mode** | [**GetShareAccountsChargePaymentMode**](GetShareAccountsChargePaymentMode.md) |  | [optional] 
**penalty** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_share_accounts_charge_options import GetShareAccountsChargeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetShareAccountsChargeOptions from a JSON string
get_share_accounts_charge_options_instance = GetShareAccountsChargeOptions.from_json(json)
# print the JSON string representation of the object
print(GetShareAccountsChargeOptions.to_json())

# convert the object into a dict
get_share_accounts_charge_options_dict = get_share_accounts_charge_options_instance.to_dict()
# create an instance of GetShareAccountsChargeOptions from a dict
get_share_accounts_charge_options_from_dict = GetShareAccountsChargeOptions.from_dict(get_share_accounts_charge_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


