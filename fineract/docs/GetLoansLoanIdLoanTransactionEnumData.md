# GetLoansLoanIdLoanTransactionEnumData

Transaction type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrual** | **bool** |  | [optional] 
**approve_transfer** | **bool** |  | [optional] 
**charge_adjustment** | **bool** |  | [optional] 
**charge_payment** | **bool** |  | [optional] 
**chargeoff** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**contra** | **bool** |  | [optional] 
**credit_balance_refund** | **bool** |  | [optional] 
**disbursement** | **bool** |  | [optional] 
**goodwill_credit** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**initiate_transfer** | **bool** |  | [optional] 
**merchant_issued_refund** | **bool** |  | [optional] 
**payout_refund** | **bool** |  | [optional] 
**recovery_repayment** | **bool** |  | [optional] 
**refund** | **bool** |  | [optional] 
**refund_for_active_loans** | **bool** |  | [optional] 
**reject_transfer** | **bool** |  | [optional] 
**repayment** | **bool** |  | [optional] 
**repayment_at_disbursement** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**waive_charges** | **bool** |  | [optional] 
**waive_interest** | **bool** |  | [optional] 
**withdraw_transfer** | **bool** |  | [optional] 
**write_off** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_loan_transaction_enum_data import GetLoansLoanIdLoanTransactionEnumData

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdLoanTransactionEnumData from a JSON string
get_loans_loan_id_loan_transaction_enum_data_instance = GetLoansLoanIdLoanTransactionEnumData.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdLoanTransactionEnumData.to_json())

# convert the object into a dict
get_loans_loan_id_loan_transaction_enum_data_dict = get_loans_loan_id_loan_transaction_enum_data_instance.to_dict()
# create an instance of GetLoansLoanIdLoanTransactionEnumData from a dict
get_loans_loan_id_loan_transaction_enum_data_from_dict = GetLoansLoanIdLoanTransactionEnumData.from_dict(get_loans_loan_id_loan_transaction_enum_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


