# PostSavingsAccountsAccountIdRequest

PostSavingsAccountsAccountIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_on_date** | **str** |  | [optional] 
**approved_on_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_savings_accounts_account_id_request import PostSavingsAccountsAccountIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSavingsAccountsAccountIdRequest from a JSON string
post_savings_accounts_account_id_request_instance = PostSavingsAccountsAccountIdRequest.from_json(json)
# print the JSON string representation of the object
print(PostSavingsAccountsAccountIdRequest.to_json())

# convert the object into a dict
post_savings_accounts_account_id_request_dict = post_savings_accounts_account_id_request_instance.to_dict()
# create an instance of PostSavingsAccountsAccountIdRequest from a dict
post_savings_accounts_account_id_request_from_dict = PostSavingsAccountsAccountIdRequest.from_dict(post_savings_accounts_account_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


