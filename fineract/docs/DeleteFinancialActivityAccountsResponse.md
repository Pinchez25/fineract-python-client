# DeleteFinancialActivityAccountsResponse

DeleteFinancialActivityAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_financial_activity_accounts_response import DeleteFinancialActivityAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFinancialActivityAccountsResponse from a JSON string
delete_financial_activity_accounts_response_instance = DeleteFinancialActivityAccountsResponse.from_json(json)
# print the JSON string representation of the object
print DeleteFinancialActivityAccountsResponse.to_json()

# convert the object into a dict
delete_financial_activity_accounts_response_dict = delete_financial_activity_accounts_response_instance.to_dict()
# create an instance of DeleteFinancialActivityAccountsResponse from a dict
delete_financial_activity_accounts_response_form_dict = delete_financial_activity_accounts_response.from_dict(delete_financial_activity_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


