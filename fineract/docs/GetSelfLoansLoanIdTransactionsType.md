# GetSelfLoansLoanIdTransactionsType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**contra** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**disbursement** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**recovery_repayment** | **bool** |  | [optional] 
**repayment** | **bool** |  | [optional] 
**repayment_at_disbursement** | **bool** |  | [optional] 
**waive_charges** | **bool** |  | [optional] 
**waive_interest** | **bool** |  | [optional] 
**write_off** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_loans_loan_id_transactions_type import GetSelfLoansLoanIdTransactionsType

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfLoansLoanIdTransactionsType from a JSON string
get_self_loans_loan_id_transactions_type_instance = GetSelfLoansLoanIdTransactionsType.from_json(json)
# print the JSON string representation of the object
print GetSelfLoansLoanIdTransactionsType.to_json()

# convert the object into a dict
get_self_loans_loan_id_transactions_type_dict = get_self_loans_loan_id_transactions_type_instance.to_dict()
# create an instance of GetSelfLoansLoanIdTransactionsType from a dict
get_self_loans_loan_id_transactions_type_form_dict = get_self_loans_loan_id_transactions_type.from_dict(get_self_loans_loan_id_transactions_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


