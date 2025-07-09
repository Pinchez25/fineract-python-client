# SavingsAccountChargeData


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
**annual_fee** | **bool** |  | [optional] 
**charge_calculation_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**charge_data** | [**ChargeData**](ChargeData.md) |  | [optional] 
**charge_id** | **int** |  | [optional] 
**charge_options** | [**List[ChargeData]**](ChargeData.md) |  | [optional] 
**charge_time_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**currency** | [**CurrencyData**](CurrencyData.md) |  | [optional] 
**due_date** | **date** |  | [optional] 
**fee_charge** | **bool** |  | [optional] 
**fee_interval** | **int** |  | [optional] 
**fee_on_month_day** | [**ChargeFeeOnMonthDay**](ChargeFeeOnMonthDay.md) |  | [optional] 
**free_withdrawal_charge_frequency** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**inactivation_date** | **date** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_free_withdrawal** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**penalty** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 
**restart_frequency** | **int** |  | [optional] 
**restart_frequency_enum** | **int** |  | [optional] 
**savings_activation** | **bool** |  | [optional] 
**withdrawal_fee** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.savings_account_charge_data import SavingsAccountChargeData

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsAccountChargeData from a JSON string
savings_account_charge_data_instance = SavingsAccountChargeData.from_json(json)
# print the JSON string representation of the object
print(SavingsAccountChargeData.to_json())

# convert the object into a dict
savings_account_charge_data_dict = savings_account_charge_data_instance.to_dict()
# create an instance of SavingsAccountChargeData from a dict
savings_account_charge_data_from_dict = SavingsAccountChargeData.from_dict(savings_account_charge_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


