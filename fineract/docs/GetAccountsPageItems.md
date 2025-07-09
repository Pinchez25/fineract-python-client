# GetAccountsPageItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**currency** | [**GetAccountsChargesCurrency**](GetAccountsChargesCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**purchased_shares** | [**List[GetAccountsTypePurchasedShares]**](GetAccountsTypePurchasedShares.md) |  | [optional] 
**status** | [**GetAccountsTypeStatus**](GetAccountsTypeStatus.md) |  | [optional] 
**summary** | [**GetAccountsTypeSummary**](GetAccountsTypeSummary.md) |  | [optional] 
**timeline** | [**GetAccountsTypeTimeline**](GetAccountsTypeTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_page_items import GetAccountsPageItems

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsPageItems from a JSON string
get_accounts_page_items_instance = GetAccountsPageItems.from_json(json)
# print the JSON string representation of the object
print GetAccountsPageItems.to_json()

# convert the object into a dict
get_accounts_page_items_dict = get_accounts_page_items_instance.to_dict()
# create an instance of GetAccountsPageItems from a dict
get_accounts_page_items_form_dict = get_accounts_page_items.from_dict(get_accounts_page_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


