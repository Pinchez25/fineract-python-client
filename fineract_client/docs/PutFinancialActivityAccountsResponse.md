# PutFinancialActivityAccountsResponse

PutFinancialActivityAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**PutFinancialActivityAccountscommentsSwagger**](PutFinancialActivityAccountscommentsSwagger.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_financial_activity_accounts_response import PutFinancialActivityAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutFinancialActivityAccountsResponse from a JSON string
put_financial_activity_accounts_response_instance = PutFinancialActivityAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(PutFinancialActivityAccountsResponse.to_json())

# convert the object into a dict
put_financial_activity_accounts_response_dict = put_financial_activity_accounts_response_instance.to_dict()
# create an instance of PutFinancialActivityAccountsResponse from a dict
put_financial_activity_accounts_response_from_dict = PutFinancialActivityAccountsResponse.from_dict(put_financial_activity_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


