# GetAccountsTypeResponse

GetAccountsTypeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_items** | [**List[GetAccountsPageItems]**](GetAccountsPageItems.md) |  | [optional] 
**total_filtered_records** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_type_response import GetAccountsTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsTypeResponse from a JSON string
get_accounts_type_response_instance = GetAccountsTypeResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccountsTypeResponse.to_json())

# convert the object into a dict
get_accounts_type_response_dict = get_accounts_type_response_instance.to_dict()
# create an instance of GetAccountsTypeResponse from a dict
get_accounts_type_response_from_dict = GetAccountsTypeResponse.from_dict(get_accounts_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


