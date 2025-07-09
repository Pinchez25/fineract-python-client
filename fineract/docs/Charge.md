# Charge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**GLAccount**](GLAccount.md) |  | [optional] 
**active** | **bool** |  | [optional] 
**allowed_client_charge_calculation_type** | **bool** |  | [optional] 
**allowed_client_charge_time** | **bool** |  | [optional] 
**allowed_loan_charge_time** | **bool** |  | [optional] 
**allowed_savings_charge_calculation_type** | **bool** |  | [optional] 
**allowed_savings_charge_time** | **bool** |  | [optional] 
**amount** | **float** |  | [optional] 
**annual_fee** | **bool** |  | [optional] 
**charge_calculation** | **int** |  | [optional] 
**charge_payment_mode** | **int** |  | [optional] 
**charge_time_type** | **int** |  | [optional] 
**client_charge** | **bool** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**disbursement_charge** | **bool** |  | [optional] 
**enable_free_withdrawal** | **bool** |  | [optional] 
**enable_payment_type** | **bool** |  | [optional] 
**fee_interval** | **int** |  | [optional] 
**fee_on_month_day** | [**ChargeFeeOnMonthDay**](ChargeFeeOnMonthDay.md) |  | [optional] 
**frequency_free_withdrawal_charge** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**income_account_id** | **int** |  | [optional] 
**loan_charge** | **bool** |  | [optional] 
**max_cap** | **float** |  | [optional] 
**min_cap** | **float** |  | [optional] 
**monthly_fee** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**overdue_installment** | **bool** |  | [optional] 
**payment_type** | [**PaymentType**](PaymentType.md) |  | [optional] 
**penalty** | **bool** |  | [optional] 
**percentage_of_approved_amount** | **bool** |  | [optional] 
**percentage_of_disbursement_amount** | **bool** |  | [optional] 
**restart_frequency** | **int** |  | [optional] 
**restart_frequency_enum** | **int** |  | [optional] 
**savings_charge** | **bool** |  | [optional] 
**tax_group** | [**TaxGroup**](TaxGroup.md) |  | [optional] 

## Example

```python
from fineract_client.models.charge import Charge

# TODO update the JSON string below
json = "{}"
# create an instance of Charge from a JSON string
charge_instance = Charge.from_json(json)
# print the JSON string representation of the object
print Charge.to_json()

# convert the object into a dict
charge_dict = charge_instance.to_dict()
# create an instance of Charge from a dict
charge_form_dict = charge.from_dict(charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


