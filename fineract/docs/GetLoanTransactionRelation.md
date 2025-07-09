# GetLoanTransactionRelation


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
from fineract_client.models.get_loan_transaction_relation import GetLoanTransactionRelation

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanTransactionRelation from a JSON string
get_loan_transaction_relation_instance = GetLoanTransactionRelation.from_json(json)
# print the JSON string representation of the object
print GetLoanTransactionRelation.to_json()

# convert the object into a dict
get_loan_transaction_relation_dict = get_loan_transaction_relation_instance.to_dict()
# create an instance of GetLoanTransactionRelation from a dict
get_loan_transaction_relation_form_dict = get_loan_transaction_relation.from_dict(get_loan_transaction_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


