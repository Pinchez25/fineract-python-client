# GetCentersSavingsAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**account_type** | [**GetCentersAccountType**](GetCentersAccountType.md) |  | [optional] 
**currency** | [**GetCentersCenterIdCurrency**](GetCentersCenterIdCurrency.md) |  | [optional] 
**deposit_type** | [**GetCentersDepositType**](GetCentersDepositType.md) |  | [optional] 
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**GetCentersCenterIdStatus**](GetCentersCenterIdStatus.md) |  | [optional] 
**timeline** | [**GetCentersTimeline**](GetCentersTimeline.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_savings_accounts import GetCentersSavingsAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersSavingsAccounts from a JSON string
get_centers_savings_accounts_instance = GetCentersSavingsAccounts.from_json(json)
# print the JSON string representation of the object
print(GetCentersSavingsAccounts.to_json())

# convert the object into a dict
get_centers_savings_accounts_dict = get_centers_savings_accounts_instance.to_dict()
# create an instance of GetCentersSavingsAccounts from a dict
get_centers_savings_accounts_from_dict = GetCentersSavingsAccounts.from_dict(get_centers_savings_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


