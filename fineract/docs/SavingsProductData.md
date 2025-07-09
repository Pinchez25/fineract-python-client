# SavingsProductData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrual_based_accounting_enabled** | **bool** |  | [optional] 
**allow_overdraft** | **bool** |  | [optional] 
**cash_based_accounting_enabled** | **bool** |  | [optional] 
**currency** | [**CurrencyData**](CurrencyData.md) |  | [optional] 
**deposit_account_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**interest_calculation_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**interest_compounding_period_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**interest_posting_period_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**lockin_period_frequency** | **int** |  | [optional] 
**lockin_period_frequency_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**max_allowed_lien_limit** | **float** |  | [optional] 
**min_required_balance** | **float** |  | [optional] 
**min_required_opening_balance** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**nominal_annual_interest_rate** | **float** |  | [optional] 
**overdraft_limit** | **float** |  | [optional] 
**periodic_accrual_accounting** | **bool** |  | [optional] 
**upfront_accrual_accounting** | **bool** |  | [optional] 
**withdrawal_fee_for_transfers** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.savings_product_data import SavingsProductData

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsProductData from a JSON string
savings_product_data_instance = SavingsProductData.from_json(json)
# print the JSON string representation of the object
print(SavingsProductData.to_json())

# convert the object into a dict
savings_product_data_dict = savings_product_data_instance.to_dict()
# create an instance of SavingsProductData from a dict
savings_product_data_from_dict = SavingsProductData.from_dict(savings_product_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


