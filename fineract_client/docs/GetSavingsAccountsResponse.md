# GetSavingsAccountsResponse

GetSavingsAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetSavingsPageItems]**](GetSavingsPageItems.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_accounts_response import GetSavingsAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsAccountsResponse from a JSON string
get_savings_accounts_response_instance = GetSavingsAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSavingsAccountsResponse.to_json())

# convert the object into a dict
get_savings_accounts_response_dict = get_savings_accounts_response_instance.to_dict()
# create an instance of GetSavingsAccountsResponse from a dict
get_savings_accounts_response_from_dict = GetSavingsAccountsResponse.from_dict(get_savings_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


