# SavingsAccountTransactionsSearchResponse

SavingsAccountTransactionsSearchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[GetSavingsAccountTransactionsPageItem]**](GetSavingsAccountTransactionsPageItem.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.savings_account_transactions_search_response import SavingsAccountTransactionsSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsAccountTransactionsSearchResponse from a JSON string
savings_account_transactions_search_response_instance = SavingsAccountTransactionsSearchResponse.from_json(json)
# print the JSON string representation of the object
print(SavingsAccountTransactionsSearchResponse.to_json())

# convert the object into a dict
savings_account_transactions_search_response_dict = savings_account_transactions_search_response_instance.to_dict()
# create an instance of SavingsAccountTransactionsSearchResponse from a dict
savings_account_transactions_search_response_from_dict = SavingsAccountTransactionsSearchResponse.from_dict(savings_account_transactions_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


