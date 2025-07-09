# CreditDebit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**gl_account_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.credit_debit import CreditDebit

# TODO update the JSON string below
json = "{}"
# create an instance of CreditDebit from a JSON string
credit_debit_instance = CreditDebit.from_json(json)
# print the JSON string representation of the object
print CreditDebit.to_json()

# convert the object into a dict
credit_debit_dict = credit_debit_instance.to_dict()
# create an instance of CreditDebit from a dict
credit_debit_form_dict = credit_debit.from_dict(credit_debit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


