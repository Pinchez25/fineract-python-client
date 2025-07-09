# GetLoansLoanIdLoanTransactionRelation

List of GetLoansLoanIdLoanTransactionRelationData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**from_loan_transaction** | **int** |  | [optional] 
**payment_type** | **str** |  | [optional] 
**relation_type** | **str** |  | [optional] 
**to_loan_charge** | **int** |  | [optional] 
**to_loan_transaction** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_loan_id_loan_transaction_relation import GetLoansLoanIdLoanTransactionRelation

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansLoanIdLoanTransactionRelation from a JSON string
get_loans_loan_id_loan_transaction_relation_instance = GetLoansLoanIdLoanTransactionRelation.from_json(json)
# print the JSON string representation of the object
print(GetLoansLoanIdLoanTransactionRelation.to_json())

# convert the object into a dict
get_loans_loan_id_loan_transaction_relation_dict = get_loans_loan_id_loan_transaction_relation_instance.to_dict()
# create an instance of GetLoansLoanIdLoanTransactionRelation from a dict
get_loans_loan_id_loan_transaction_relation_from_dict = GetLoansLoanIdLoanTransactionRelation.from_dict(get_loans_loan_id_loan_transaction_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


