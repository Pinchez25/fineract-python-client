# GetShareAccountsClientIdProductIdResponse

GetShareAccountsClientIdProductIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_options** | [**List[GetClientIdProductIdChargeOptions]**](GetClientIdProductIdChargeOptions.md) |  | [optional] 
**product_options** | [**List[GetClientIdProductIdProductOptions]**](GetClientIdProductIdProductOptions.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_share_accounts_client_id_product_id_response import GetShareAccountsClientIdProductIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetShareAccountsClientIdProductIdResponse from a JSON string
get_share_accounts_client_id_product_id_response_instance = GetShareAccountsClientIdProductIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetShareAccountsClientIdProductIdResponse.to_json())

# convert the object into a dict
get_share_accounts_client_id_product_id_response_dict = get_share_accounts_client_id_product_id_response_instance.to_dict()
# create an instance of GetShareAccountsClientIdProductIdResponse from a dict
get_share_accounts_client_id_product_id_response_from_dict = GetShareAccountsClientIdProductIdResponse.from_dict(get_share_accounts_client_id_product_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


