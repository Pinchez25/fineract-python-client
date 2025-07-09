# GetAccountsTypePurchasedShares


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**number_of_shares** | **int** |  | [optional] 
**purchased_date** | **str** |  | [optional] 
**purchased_price** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_type_purchased_shares import GetAccountsTypePurchasedShares

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsTypePurchasedShares from a JSON string
get_accounts_type_purchased_shares_instance = GetAccountsTypePurchasedShares.from_json(json)
# print the JSON string representation of the object
print GetAccountsTypePurchasedShares.to_json()

# convert the object into a dict
get_accounts_type_purchased_shares_dict = get_accounts_type_purchased_shares_instance.to_dict()
# create an instance of GetAccountsTypePurchasedShares from a dict
get_accounts_type_purchased_shares_form_dict = get_accounts_type_purchased_shares.from_dict(get_accounts_type_purchased_shares_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


