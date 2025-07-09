# GetAccountsPurchasedSharesStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_purchased_shares_status import GetAccountsPurchasedSharesStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsPurchasedSharesStatus from a JSON string
get_accounts_purchased_shares_status_instance = GetAccountsPurchasedSharesStatus.from_json(json)
# print the JSON string representation of the object
print(GetAccountsPurchasedSharesStatus.to_json())

# convert the object into a dict
get_accounts_purchased_shares_status_dict = get_accounts_purchased_shares_status_instance.to_dict()
# create an instance of GetAccountsPurchasedSharesStatus from a dict
get_accounts_purchased_shares_status_from_dict = GetAccountsPurchasedSharesStatus.from_dict(get_accounts_purchased_shares_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


