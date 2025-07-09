# GetPocketLoanAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**account_number** | **int** |  | [optional] 
**account_type** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**pocket_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_pocket_loan_accounts import GetPocketLoanAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetPocketLoanAccounts from a JSON string
get_pocket_loan_accounts_instance = GetPocketLoanAccounts.from_json(json)
# print the JSON string representation of the object
print(GetPocketLoanAccounts.to_json())

# convert the object into a dict
get_pocket_loan_accounts_dict = get_pocket_loan_accounts_instance.to_dict()
# create an instance of GetPocketLoanAccounts from a dict
get_pocket_loan_accounts_from_dict = GetPocketLoanAccounts.from_dict(get_pocket_loan_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


