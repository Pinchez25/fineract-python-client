# GetLoansLoanIdTransactions

Set of GetLoansLoanIdTransactions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_number** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**bank_number** | **int** |  | [optional] 
**check_number** | **int** |  | [optional] 
**currency** | [**GetLoansLoanIdCurrency**](GetLoansLoanIdCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**date_format** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fee_charges_portion** | **float** |  | [optional] 
**fixed_emi_amount** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_portion** | **float** |  | [optional] 
**loan_charge_paid_by_list** | [**List[GetLoansLoanIdLoanChargePaidByData]**](GetLoansLoanIdLoanChargePaidByData.md) | List of GetLoansLoanIdLoanChargePaidByData | [optional] 
**loan_repayment_schedule_installments** | [**List[GetLoansLoanIdLoanRepaymentScheduleInstallmentData]**](GetLoansLoanIdLoanRepaymentScheduleInstallmentData.md) | List of GetLoansLoanIdLoanRepaymentScheduleInstallmentData | [optional] 
**locale** | **str** |  | [optional] 
**manually_reversed** | **bool** |  | [optional] 
**net_disbursal_amount** | **float** |  | [optional] 
**number_of_repayments** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**outstanding_loan_balance** | **float** |  | [optional] 
**overpayment_portion** | **float** |  | [optional] 
**payment_detail_data** | [**GetLoansLoanIdPaymentDetailData**](GetLoansLoanIdPaymentDetailData.md) |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**payment_type_options** | [**List[GetLoansLoanIdPaymentType]**](GetLoansLoanIdPaymentType.md) | List of GetLoansLoanIdPaymentType | [optional] 
**penalty_charges_portion** | **float** |  | [optional] 
**possible_next_repayment_date** | **date** |  | [optional] 
**principal_portion** | **float** |  | [optional] 
**receipt_number** | **int** |  | [optional] 
**reversal_external_id** | **str** |  | [optional] 
**reversed_on_date** | **date** |  | [optional] 
**routing_code** | **int** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**transaction_amount** | **float** |  | [optional] 
**transaction_date** | **date** |  | [optional] 
**transaction_relations** | [**List[GetLoansLoanIdLoanTransactionRelation]**](GetLoansLoanIdLoanTransactionRelation.md) | List of GetLoansLoanIdLoanTransactionRelationData | [optional] 
**transaction_type** | **str** |  | [optional] 
**type** | [**GetLoansLoanIdLoanTransactionEnumData**](GetLoansLoanIdLoanTransactionEnumData.md) |  | [optional] 
**unrecognized_income_portion** | **float** |  | [optional] 
**write_off_reason_options** | [**List[GetLoansLoanIdCodeValueData]**](GetLoansLoanIdCodeValueData.md) | List of GetLoansLoanIdCodeValueData | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_transactions import GetLoansLoanIdTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdTransactions from a JSON string
get_loans_loan_id_transactions_instance = GetLoansLoanIdTransactions.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdTransactions.to_json())

# convert the object into a dict
get_loans_loan_id_transactions_dict = get_loans_loan_id_transactions_instance.to_dict()
# create an instance of GetLoansLoanIdTransactions from a dict
get_loans_loan_id_transactions_from_dict = GetLoansLoanIdTransactions.from_dict(get_loans_loan_id_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


