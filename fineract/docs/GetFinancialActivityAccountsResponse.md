# GetFinancialActivityAccountsResponse

GetFinancialActivityAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**financial_activity_data** | [**FinancialActivityData**](FinancialActivityData.md) |  | [optional] 
**gl_account_data** | [**GLAccountData**](GLAccountData.md) |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_financial_activity_accounts_response import GetFinancialActivityAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFinancialActivityAccountsResponse from a JSON string
get_financial_activity_accounts_response_instance = GetFinancialActivityAccountsResponse.from_json(json)
# print the JSON string representation of the object
print GetFinancialActivityAccountsResponse.to_json()

# convert the object into a dict
get_financial_activity_accounts_response_dict = get_financial_activity_accounts_response_instance.to_dict()
# create an instance of GetFinancialActivityAccountsResponse from a dict
get_financial_activity_accounts_response_form_dict = get_financial_activity_accounts_response.from_dict(get_financial_activity_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


