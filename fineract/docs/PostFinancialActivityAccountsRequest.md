# PostFinancialActivityAccountsRequest

PostFinancialActivityAccountsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**financial_activity_id** | **int** |  | [optional] 
**gl_account_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_financial_activity_accounts_request import PostFinancialActivityAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFinancialActivityAccountsRequest from a JSON string
post_financial_activity_accounts_request_instance = PostFinancialActivityAccountsRequest.from_json(json)
# print the JSON string representation of the object
print(PostFinancialActivityAccountsRequest.to_json())

# convert the object into a dict
post_financial_activity_accounts_request_dict = post_financial_activity_accounts_request_instance.to_dict()
# create an instance of PostFinancialActivityAccountsRequest from a dict
post_financial_activity_accounts_request_from_dict = PostFinancialActivityAccountsRequest.from_dict(post_financial_activity_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


