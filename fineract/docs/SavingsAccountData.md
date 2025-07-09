# SavingsAccountData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**accrual_based_accounting_enabled_on_savings_product** | **bool** |  | [optional] 
**activated_on_date** | **date** |  | [optional] 
**activation_local_date** | **date** |  | [optional] 
**allow_overdraft** | **bool** |  | [optional] 
**annual_fee** | [**SavingsAccountChargeData**](SavingsAccountChargeData.md) |  | [optional] 
**cash_based_accounting_enabled_on_savings_product** | **bool** |  | [optional] 
**charge_options** | [**List[ChargeData]**](ChargeData.md) |  | [optional] 
**charges** | [**List[SavingsAccountChargeData]**](SavingsAccountChargeData.md) |  | [optional] 
**client_data** | [**ClientData**](ClientData.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**currency** | [**CurrencyData**](CurrencyData.md) |  | [optional] 
**datatables** | [**List[DatatableData]**](DatatableData.md) |  | [optional] 
**date_format** | **str** |  | [optional] 
**days_to_dormancy** | **int** |  | [optional] 
**days_to_escheat** | **int** |  | [optional] 
**days_to_inactive** | **int** |  | [optional] 
**deposit_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**deposit_type_id** | **int** |  | [optional] 
**enforce_min_required_balance** | **bool** |  | [optional] 
**existing_reversed_transaction_ids** | **List[int]** |  | [optional] 
**existing_transaction_ids** | **List[int]** |  | [optional] 
**external_id** | **str** |  | [optional] 
**field_officer_id** | **int** |  | [optional] 
**field_officer_name** | **str** |  | [optional] 
**field_officer_options** | [**List[StaffData]**](StaffData.md) |  | [optional] 
**gl_account_id_for_interest_on_savings** | **int** |  | [optional] 
**gl_account_id_for_savings_control** | **int** |  | [optional] 
**group_general_data** | [**GroupGeneralData**](GroupGeneralData.md) |  | [optional] 
**group_id** | **int** |  | [optional] 
**group_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**interest_calculation_days_in_year_type_id** | **int** |  | [optional] 
**interest_calculation_days_in_year_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**interest_calculation_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**interest_calculation_type_id** | **int** |  | [optional] 
**interest_calculation_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**interest_compounding_period_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**interest_compounding_period_type_id** | **int** |  | [optional] 
**interest_compounding_period_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**interest_posting_period_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**interest_posting_period_type_id** | **int** |  | [optional] 
**interest_posting_period_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**is_dormancy_tracking_active** | **bool** |  | [optional] 
**last_active_transaction_date** | **date** |  | [optional] 
**last_savings_account_transaction** | [**SavingsAccountTransactionData**](SavingsAccountTransactionData.md) |  | [optional] 
**lien_allowed** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**locked_in_until_date** | **date** |  | [optional] 
**lockin_period_frequency** | **int** |  | [optional] 
**lockin_period_frequency_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**lockin_period_frequency_type_id** | **int** |  | [optional] 
**lockin_period_frequency_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**max_allowed_lien_limit** | **float** |  | [optional] 
**min_balance_for_interest_calculation** | **float** |  | [optional] 
**min_overdraft_for_interest_calculation** | **float** |  | [optional] 
**min_required_balance** | **float** |  | [optional] 
**min_required_opening_balance** | **float** |  | [optional] 
**new_savings_account_transaction_data** | [**List[SavingsAccountTransactionData]**](SavingsAccountTransactionData.md) |  | [optional] 
**nominal_annual_interest_rate** | **float** |  | [optional] 
**nominal_annual_interest_rate_overdraft** | **float** |  | [optional] 
**office_id** | **int** |  | [optional] 
**on_hold_funds** | **float** |  | [optional] 
**overdraft_limit** | **float** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_options** | [**List[SavingsProductData]**](SavingsProductData.md) |  | [optional] 
**reason_for_block** | **str** |  | [optional] 
**row_index** | **int** |  | [optional] 
**savings_account_summary_data** | [**SavingsAccountSummaryData**](SavingsAccountSummaryData.md) |  | [optional] 
**savings_account_transaction_data** | [**List[SavingsAccountTransactionData]**](SavingsAccountTransactionData.md) |  | [optional] 
**savings_account_transaction_summary_wrapper** | **object** |  | [optional] 
**savings_account_transactions_with_pivot_config** | [**List[SavingsAccountTransactionData]**](SavingsAccountTransactionData.md) |  | [optional] 
**savings_amount_on_hold** | **float** |  | [optional] 
**savings_helper** | **object** |  | [optional] 
**savings_product** | [**SavingsProductData**](SavingsProductData.md) |  | [optional] 
**savings_product_data** | [**SavingsProductData**](SavingsProductData.md) |  | [optional] 
**savings_product_id** | **int** |  | [optional] 
**savings_product_name** | **str** |  | [optional] 
**start_interest_calculation_date** | **date** |  | [optional] 
**status** | [**SavingsAccountStatusEnumData**](SavingsAccountStatusEnumData.md) |  | [optional] 
**sub_status** | [**SavingsAccountSubStatusEnumData**](SavingsAccountSubStatusEnumData.md) |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**summary** | [**SavingsAccountSummaryData**](SavingsAccountSummaryData.md) |  | [optional] 
**tax_group** | [**TaxGroupData**](TaxGroupData.md) |  | [optional] 
**timeline** | [**SavingsAccountApplicationTimelineData**](SavingsAccountApplicationTimelineData.md) |  | [optional] 
**transactions** | [**List[SavingsAccountTransactionData]**](SavingsAccountTransactionData.md) |  | [optional] 
**updated_transactions** | [**List[SavingsAccountTransactionData]**](SavingsAccountTransactionData.md) |  | [optional] 
**with_hold_tax** | **bool** |  | [optional] 
**withdrawal_fee** | [**SavingsAccountChargeData**](SavingsAccountChargeData.md) |  | [optional] 
**withdrawal_fee_for_transfers** | **bool** |  | [optional] 
**withdrawal_fee_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.savings_account_data import SavingsAccountData

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsAccountData from a JSON string
savings_account_data_instance = SavingsAccountData.from_json(json)
# print the JSON string representation of the object
print(SavingsAccountData.to_json())

# convert the object into a dict
savings_account_data_dict = savings_account_data_instance.to_dict()
# create an instance of SavingsAccountData from a dict
savings_account_data_from_dict = SavingsAccountData.from_dict(savings_account_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


