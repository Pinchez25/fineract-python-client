# SavingsAccountTransactionEnumData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrual** | **bool** |  | [optional] 
**amount_hold** | **bool** |  | [optional] 
**amount_release** | **bool** |  | [optional] 
**annual_fee** | **bool** |  | [optional] 
**approve_transfer** | **bool** |  | [optional] 
**charge_transaction** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**credit** | **bool** |  | [optional] 
**debit** | **bool** |  | [optional] 
**deposit** | **bool** |  | [optional] 
**deposit_or_withdrawal** | **bool** |  | [optional] 
**dividend_payout** | **bool** |  | [optional] 
**entry_type** | **str** |  | [optional] 
**escheat** | **bool** |  | [optional] 
**fee_deduction** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**income_from_interest** | **bool** |  | [optional] 
**initiate_transfer** | **bool** |  | [optional] 
**interest_posting** | **bool** |  | [optional] 
**over_draft_interest_posting** | **bool** |  | [optional] 
**overdraft_fee** | **bool** |  | [optional] 
**overdraft_interest** | **bool** |  | [optional] 
**pay_charge** | **bool** |  | [optional] 
**reject_transfer** | **bool** |  | [optional] 
**transaction_type_enum** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**withdraw_transfer** | **bool** |  | [optional] 
**withdrawal** | **bool** |  | [optional] 
**withdrawal_fee** | **bool** |  | [optional] 
**withhold_tax** | **bool** |  | [optional] 
**writtenoff** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.savings_account_transaction_enum_data import SavingsAccountTransactionEnumData

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsAccountTransactionEnumData from a JSON string
savings_account_transaction_enum_data_instance = SavingsAccountTransactionEnumData.from_json(json)
# print the JSON string representation of the object
print SavingsAccountTransactionEnumData.to_json()

# convert the object into a dict
savings_account_transaction_enum_data_dict = savings_account_transaction_enum_data_instance.to_dict()
# create an instance of SavingsAccountTransactionEnumData from a dict
savings_account_transaction_enum_data_form_dict = savings_account_transaction_enum_data.from_dict(savings_account_transaction_enum_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


