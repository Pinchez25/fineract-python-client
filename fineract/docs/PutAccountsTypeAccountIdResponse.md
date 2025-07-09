# PutAccountsTypeAccountIdResponse

PutAccountsTypeAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutAccountsChanges**](PutAccountsChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_accounts_type_account_id_response import PutAccountsTypeAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutAccountsTypeAccountIdResponse from a JSON string
put_accounts_type_account_id_response_instance = PutAccountsTypeAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print PutAccountsTypeAccountIdResponse.to_json()

# convert the object into a dict
put_accounts_type_account_id_response_dict = put_accounts_type_account_id_response_instance.to_dict()
# create an instance of PutAccountsTypeAccountIdResponse from a dict
put_accounts_type_account_id_response_form_dict = put_accounts_type_account_id_response.from_dict(put_accounts_type_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


