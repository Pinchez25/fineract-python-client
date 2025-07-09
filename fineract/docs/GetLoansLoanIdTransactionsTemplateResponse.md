# GetLoansLoanIdTransactionsTemplateResponse

GetLoansLoanIdTransactionsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | [**GetLoanCurrency**](GetLoanCurrency.md) |  | [optional] 
**var_date** | **date** |  | [optional] 
**total** | [**GetLoansTotal**](GetLoansTotal.md) |  | [optional] 
**transaction_type** | [**GetLoansTransactionType**](GetLoansTransactionType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_transactions_template_response import GetLoansLoanIdTransactionsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdTransactionsTemplateResponse from a JSON string
get_loans_loan_id_transactions_template_response_instance = GetLoansLoanIdTransactionsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetLoansLoanIdTransactionsTemplateResponse.to_json()

# convert the object into a dict
get_loans_loan_id_transactions_template_response_dict = get_loans_loan_id_transactions_template_response_instance.to_dict()
# create an instance of GetLoansLoanIdTransactionsTemplateResponse from a dict
get_loans_loan_id_transactions_template_response_form_dict = get_loans_loan_id_transactions_template_response.from_dict(get_loans_loan_id_transactions_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


