# GetSelfLoansLoanIdTransactionsTransactionIdResponse

GetSelfLoansLoanIdTransactionsTransactionIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | [**GetLoanCurrency**](GetLoanCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**interest_portion** | **float** |  | [optional] 
**manually_reversed** | **bool** |  | [optional] 
**type** | [**GetSelfLoansLoanIdTransactionsType**](GetSelfLoansLoanIdTransactionsType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_self_loans_loan_id_transactions_transaction_id_response import GetSelfLoansLoanIdTransactionsTransactionIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfLoansLoanIdTransactionsTransactionIdResponse from a JSON string
get_self_loans_loan_id_transactions_transaction_id_response_instance = GetSelfLoansLoanIdTransactionsTransactionIdResponse.from_json(json)
# print the JSON string representation of the object
print GetSelfLoansLoanIdTransactionsTransactionIdResponse.to_json()

# convert the object into a dict
get_self_loans_loan_id_transactions_transaction_id_response_dict = get_self_loans_loan_id_transactions_transaction_id_response_instance.to_dict()
# create an instance of GetSelfLoansLoanIdTransactionsTransactionIdResponse from a dict
get_self_loans_loan_id_transactions_transaction_id_response_form_dict = get_self_loans_loan_id_transactions_transaction_id_response.from_dict(get_self_loans_loan_id_transactions_transaction_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


