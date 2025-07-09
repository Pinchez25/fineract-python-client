# SavingsAccountTransactionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_no** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**amount_on_hold** | **bool** |  | [optional] 
**amount_release** | **bool** |  | [optional] 
**annual_fee** | **bool** |  | [optional] 
**annual_fee_and_not_reversed** | **bool** |  | [optional] 
**balance_end_date** | **date** |  | [optional] 
**balance_number_of_days** | **int** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**charge_transaction** | **bool** |  | [optional] 
**charge_transaction_and_not_reversed** | **bool** |  | [optional] 
**charges_paid_by_data** | [**List[SavingsAccountChargesPaidByData]**](SavingsAccountChargesPaidByData.md) |  | [optional] 
**check_number** | **str** |  | [optional] 
**credit** | **bool** |  | [optional] 
**cumulative_balance** | **float** |  | [optional] 
**currency** | [**CurrencyData**](CurrencyData.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**date_format** | **str** |  | [optional] 
**debit** | **bool** |  | [optional] 
**deposit** | **bool** |  | [optional] 
**deposit_and_not_reversed** | **bool** |  | [optional] 
**dividend_payout_and_not_reversed** | **bool** |  | [optional] 
**end_of_balance_local_date** | **date** |  | [optional] 
**entry_type** | **str** |  | [optional] 
**fee_charge** | **bool** |  | [optional] 
**fee_charge_and_not_reversed** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_posting** | **bool** |  | [optional] 
**interest_posting_and_not_reversed** | **bool** |  | [optional] 
**interested_posted_as_on** | **bool** |  | [optional] 
**is_manual_transaction** | **bool** |  | [optional] 
**is_reversal** | **bool** |  | [optional] 
**lien_transaction** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**manual_transaction** | **bool** |  | [optional] 
**modified_id** | **int** |  | [optional] 
**not_reversed** | **bool** |  | [optional] 
**note** | **str** |  | [optional] 
**original_transaction_id** | **int** |  | [optional] 
**outstanding_charge_amount** | **float** |  | [optional] 
**overdraft_amount** | **float** |  | [optional] 
**overdraft_interest_and_not_reversed** | **bool** |  | [optional] 
**pay_charge** | **bool** |  | [optional] 
**payment_detail_data** | [**PaymentDetailData**](PaymentDetailData.md) |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**payment_type_options** | [**List[PaymentTypeData]**](PaymentTypeData.md) |  | [optional] 
**penalty_charge** | **bool** |  | [optional] 
**penalty_charge_and_not_reversed** | **bool** |  | [optional] 
**reason_for_block** | **str** |  | [optional] 
**receipt_number** | **str** |  | [optional] 
**ref_no** | **str** |  | [optional] 
**release_transaction_id** | **int** |  | [optional] 
**reversal_transaction** | **bool** |  | [optional] 
**reversed** | **bool** |  | [optional] 
**routing_code** | **str** |  | [optional] 
**row_index** | **int** |  | [optional] 
**running_balance** | **float** |  | [optional] 
**savings_account_charges_paid** | [**List[SavingsAccountChargesPaidByData]**](SavingsAccountChargesPaidByData.md) |  | [optional] 
**savings_account_id** | **int** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**tax_details** | [**List[TaxDetailsData]**](TaxDetailsData.md) |  | [optional] 
**transaction_amount** | **float** |  | [optional] 
**transaction_date** | **date** |  | [optional] 
**transaction_type** | [**SavingsAccountTransactionEnumData**](SavingsAccountTransactionEnumData.md) |  | [optional] 
**transfer** | [**AccountTransferData**](AccountTransferData.md) |  | [optional] 
**waive_charge** | **bool** |  | [optional] 
**waive_fee_charge** | **bool** |  | [optional] 
**waive_fee_charge_and_not_reversed** | **bool** |  | [optional] 
**waive_penalty_charge** | **bool** |  | [optional] 
**waive_penalty_charge_and_not_reversed** | **bool** |  | [optional] 
**with_hold_tax_and_not_reversed** | **bool** |  | [optional] 
**withdrawal** | **bool** |  | [optional] 
**withdrawal_fee_and_not_reversed** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.savings_account_transaction_data import SavingsAccountTransactionData

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsAccountTransactionData from a JSON string
savings_account_transaction_data_instance = SavingsAccountTransactionData.from_json(json)
# print the JSON string representation of the object
print SavingsAccountTransactionData.to_json()

# convert the object into a dict
savings_account_transaction_data_dict = savings_account_transaction_data_instance.to_dict()
# create an instance of SavingsAccountTransactionData from a dict
savings_account_transaction_data_form_dict = savings_account_transaction_data.from_dict(savings_account_transaction_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


