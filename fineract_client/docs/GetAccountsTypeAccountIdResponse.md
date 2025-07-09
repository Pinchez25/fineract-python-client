# GetAccountsTypeAccountIdResponse

GetAccountsTypeAccountIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**allow_dividend_calculation_for_inactive_clients** | **bool** |  | [optional] 
**charges** | [**List[GetAccountsCharges]**](GetAccountsCharges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**client_name** | **str** |  | [optional] 
**currency** | [**GetAccountsCurrency**](GetAccountsCurrency.md) |  | [optional] 
**current_market_price** | **int** |  | [optional] 
**dividends** | **List[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**lock_period_type_enum** | [**GetAccountsLockPeriodTypeEnum**](GetAccountsLockPeriodTypeEnum.md) |  | [optional] 
**lockin_period** | **int** |  | [optional] 
**minimum_active_period** | **int** |  | [optional] 
**minimum_active_period_type_enum** | [**GetAccountsLockPeriodTypeEnum**](GetAccountsLockPeriodTypeEnum.md) |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**purchased_shares** | [**List[GetAccountsPurchasedShares]**](GetAccountsPurchasedShares.md) |  | [optional] 
**savings_account_id** | **int** |  | [optional] 
**savings_account_number** | **int** |  | [optional] 
**status** | [**GetAccountsStatus**](GetAccountsStatus.md) |  | [optional] 
**summary** | [**GetAccountsSummary**](GetAccountsSummary.md) |  | [optional] 
**timeline** | [**GetAccountsTimeline**](GetAccountsTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_type_account_id_response import GetAccountsTypeAccountIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsTypeAccountIdResponse from a JSON string
get_accounts_type_account_id_response_instance = GetAccountsTypeAccountIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccountsTypeAccountIdResponse.to_json())

# convert the object into a dict
get_accounts_type_account_id_response_dict = get_accounts_type_account_id_response_instance.to_dict()
# create an instance of GetAccountsTypeAccountIdResponse from a dict
get_accounts_type_account_id_response_from_dict = GetAccountsTypeAccountIdResponse.from_dict(get_accounts_type_account_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


