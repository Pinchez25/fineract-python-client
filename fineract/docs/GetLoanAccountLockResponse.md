# GetLoanAccountLockResponse

GetLoanAccountLockResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[LoanAccountLock]**](LoanAccountLock.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**page** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_loan_account_lock_response import GetLoanAccountLockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLoanAccountLockResponse from a JSON string
get_loan_account_lock_response_instance = GetLoanAccountLockResponse.from_json(json)
# print the JSON string representation of the object
print(GetLoanAccountLockResponse.to_json())

# convert the object into a dict
get_loan_account_lock_response_dict = get_loan_account_lock_response_instance.to_dict()
# create an instance of GetLoanAccountLockResponse from a dict
get_loan_account_lock_response_from_dict = GetLoanAccountLockResponse.from_dict(get_loan_account_lock_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


