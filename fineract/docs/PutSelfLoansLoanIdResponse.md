# PutSelfLoansLoanIdResponse

PutSelfLoansLoanIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutSelfLoansChanges**](PutSelfLoansChanges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_self_loans_loan_id_response import PutSelfLoansLoanIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutSelfLoansLoanIdResponse from a JSON string
put_self_loans_loan_id_response_instance = PutSelfLoansLoanIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutSelfLoansLoanIdResponse.to_json())

# convert the object into a dict
put_self_loans_loan_id_response_dict = put_self_loans_loan_id_response_instance.to_dict()
# create an instance of PutSelfLoansLoanIdResponse from a dict
put_self_loans_loan_id_response_from_dict = PutSelfLoansLoanIdResponse.from_dict(put_self_loans_loan_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


