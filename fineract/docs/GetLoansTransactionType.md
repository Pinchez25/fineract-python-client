# GetLoansTransactionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loans_transaction_type import GetLoansTransactionType

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoansTransactionType from a JSON string
get_loans_transaction_type_instance = GetLoansTransactionType.from_json(json)
# print the JSON string representation of the object
print(GetLoansTransactionType.to_json())

# convert the object into a dict
get_loans_transaction_type_dict = get_loans_transaction_type_instance.to_dict()
# create an instance of GetLoansTransactionType from a dict
get_loans_transaction_type_from_dict = GetLoansTransactionType.from_dict(get_loans_transaction_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


