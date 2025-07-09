# LoanAccountLock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**lock_owner** | **str** |  | [optional] 
**lock_placed_on** | **datetime** |  | [optional] 
**lock_placed_on_cob_business_date** | **date** |  | [optional] 
**new_lock_owner** | **str** |  | [optional] 
**stacktrace** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.loan_account_lock import LoanAccountLock

# TODO update the JSON string below
json = "{}"
# create an instance of LoanAccountLock from a JSON string
loan_account_lock_instance = LoanAccountLock.from_json(json)
# print the JSON string representation of the object
print LoanAccountLock.to_json()

# convert the object into a dict
loan_account_lock_dict = loan_account_lock_instance.to_dict()
# create an instance of LoanAccountLock from a dict
loan_account_lock_form_dict = loan_account_lock.from_dict(loan_account_lock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


