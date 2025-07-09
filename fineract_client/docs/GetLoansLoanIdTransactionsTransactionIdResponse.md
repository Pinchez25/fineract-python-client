# GetLoansLoanIdTransactionsTransactionIdResponse

GetLoansLoanIdTransactionsTransactionIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | [**GetLoansCurrency**](GetLoansCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**external_id** | **str** |  | [optional] 
**fee_charges_portion** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_portion** | **float** |  | [optional] 
**loan_charge_paid_by_list** | [**List[GetLoansLoanIdLoanChargePaidByData]**](GetLoansLoanIdLoanChargePaidByData.md) |  | [optional] 
**manually_reversed** | **bool** |  | [optional] 
**net_disbursal_amount** | **float** |  | [optional] 
**outstanding_loan_balance** | **float** |  | [optional] 
**overpayment_portion** | **float** |  | [optional] 
**payment_detail_data** | [**PaymentDetailData**](PaymentDetailData.md) |  | [optional] 
**penalty_charges_portion** | **float** |  | [optional] 
**possible_next_repayment_date** | **date** |  | [optional] 
**principal_portion** | **float** |  | [optional] 
**reversal_external_id** | **str** |  | [optional] 
**reversed_on_date** | **date** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**transaction_relations** | [**List[GetLoanTransactionRelation]**](GetLoanTransactionRelation.md) |  | [optional] 
**type** | [**GetLoansType**](GetLoansType.md) |  | [optional] 
**unrecognized_income_portion** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_transactions_transaction_id_response import GetLoansLoanIdTransactionsTransactionIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdTransactionsTransactionIdResponse from a JSON string
get_loans_loan_id_transactions_transaction_id_response_instance = GetLoansLoanIdTransactionsTransactionIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdTransactionsTransactionIdResponse.to_json())

# convert the object into a dict
get_loans_loan_id_transactions_transaction_id_response_dict = get_loans_loan_id_transactions_transaction_id_response_instance.to_dict()
# create an instance of GetLoansLoanIdTransactionsTransactionIdResponse from a dict
get_loans_loan_id_transactions_transaction_id_response_from_dict = GetLoansLoanIdTransactionsTransactionIdResponse.from_dict(get_loans_loan_id_transactions_transaction_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


