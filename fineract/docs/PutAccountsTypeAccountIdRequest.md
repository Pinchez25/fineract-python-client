# PutAccountsTypeAccountIdRequest

PutAccountsTypeAccountIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_date** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**requested_shares** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_accounts_type_account_id_request import PutAccountsTypeAccountIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutAccountsTypeAccountIdRequest from a JSON string
put_accounts_type_account_id_request_instance = PutAccountsTypeAccountIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutAccountsTypeAccountIdRequest.to_json())

# convert the object into a dict
put_accounts_type_account_id_request_dict = put_accounts_type_account_id_request_instance.to_dict()
# create an instance of PutAccountsTypeAccountIdRequest from a dict
put_accounts_type_account_id_request_from_dict = PutAccountsTypeAccountIdRequest.from_dict(put_accounts_type_account_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


