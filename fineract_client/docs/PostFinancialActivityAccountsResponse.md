# PostFinancialActivityAccountsResponse

PostFinancialActivityAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_financial_activity_accounts_response import PostFinancialActivityAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostFinancialActivityAccountsResponse from a JSON string
post_financial_activity_accounts_response_instance = PostFinancialActivityAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(PostFinancialActivityAccountsResponse.to_json())

# convert the object into a dict
post_financial_activity_accounts_response_dict = post_financial_activity_accounts_response_instance.to_dict()
# create an instance of PostFinancialActivityAccountsResponse from a dict
post_financial_activity_accounts_response_from_dict = PostFinancialActivityAccountsResponse.from_dict(post_financial_activity_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


