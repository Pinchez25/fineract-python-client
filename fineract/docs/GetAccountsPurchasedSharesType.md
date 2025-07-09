# GetAccountsPurchasedSharesType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_purchased_shares_type import GetAccountsPurchasedSharesType

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsPurchasedSharesType from a JSON string
get_accounts_purchased_shares_type_instance = GetAccountsPurchasedSharesType.from_json(json)
# print the JSON string representation of the object
print GetAccountsPurchasedSharesType.to_json()

# convert the object into a dict
get_accounts_purchased_shares_type_dict = get_accounts_purchased_shares_type_instance.to_dict()
# create an instance of GetAccountsPurchasedSharesType from a dict
get_accounts_purchased_shares_type_form_dict = get_accounts_purchased_shares_type.from_dict(get_accounts_purchased_shares_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


