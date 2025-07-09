# GetAccountsPurchasedShares


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**amount_paid** | **float** |  | [optional] 
**charge_amount** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**number_of_shares** | **int** |  | [optional] 
**purchased_date** | **date** |  | [optional] 
**purchased_price** | **float** |  | [optional] 
**status** | [**GetAccountsPurchasedSharesStatus**](GetAccountsPurchasedSharesStatus.md) |  | [optional] 
**type** | [**GetAccountsPurchasedSharesType**](GetAccountsPurchasedSharesType.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_purchased_shares import GetAccountsPurchasedShares

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsPurchasedShares from a JSON string
get_accounts_purchased_shares_instance = GetAccountsPurchasedShares.from_json(json)
# print the JSON string representation of the object
print GetAccountsPurchasedShares.to_json()

# convert the object into a dict
get_accounts_purchased_shares_dict = get_accounts_purchased_shares_instance.to_dict()
# create an instance of GetAccountsPurchasedShares from a dict
get_accounts_purchased_shares_form_dict = get_accounts_purchased_shares.from_dict(get_accounts_purchased_shares_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


