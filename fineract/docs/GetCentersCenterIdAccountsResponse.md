# GetCentersCenterIdAccountsResponse

GetCentersCenterIdAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**savings_accounts** | [**List[GetCentersSavingsAccounts]**](GetCentersSavingsAccounts.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_center_id_accounts_response import GetCentersCenterIdAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersCenterIdAccountsResponse from a JSON string
get_centers_center_id_accounts_response_instance = GetCentersCenterIdAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(GetCentersCenterIdAccountsResponse.to_json())

# convert the object into a dict
get_centers_center_id_accounts_response_dict = get_centers_center_id_accounts_response_instance.to_dict()
# create an instance of GetCentersCenterIdAccountsResponse from a dict
get_centers_center_id_accounts_response_from_dict = GetCentersCenterIdAccountsResponse.from_dict(get_centers_center_id_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


