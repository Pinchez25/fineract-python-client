# PostAccountsTypeAccountIdRequest

PostAccountsTypeAccountIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_shares** | [**List[PostAccountsRequestedShares]**](PostAccountsRequestedShares.md) |  | [optional] 

## Example

```python
from fineract_client.models.post_accounts_type_account_id_request import PostAccountsTypeAccountIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountsTypeAccountIdRequest from a JSON string
post_accounts_type_account_id_request_instance = PostAccountsTypeAccountIdRequest.from_json(json)
# print the JSON string representation of the object
print(PostAccountsTypeAccountIdRequest.to_json())

# convert the object into a dict
post_accounts_type_account_id_request_dict = post_accounts_type_account_id_request_instance.to_dict()
# create an instance of PostAccountsTypeAccountIdRequest from a dict
post_accounts_type_account_id_request_from_dict = PostAccountsTypeAccountIdRequest.from_dict(post_accounts_type_account_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


