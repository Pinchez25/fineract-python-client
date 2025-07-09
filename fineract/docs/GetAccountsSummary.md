# GetAccountsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **int** |  | [optional] 
**currency** | [**GetAccountsCurrency**](GetAccountsCurrency.md) |  | [optional] 
**id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**GetAccountsStatus**](GetAccountsStatus.md) |  | [optional] 
**timeline** | [**GetAccountsTimeline**](GetAccountsTimeline.md) |  | [optional] 
**total_approved_shares** | **int** |  | [optional] 
**total_pending_for_approval_shares** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_accounts_summary import GetAccountsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountsSummary from a JSON string
get_accounts_summary_instance = GetAccountsSummary.from_json(json)
# print the JSON string representation of the object
print GetAccountsSummary.to_json()

# convert the object into a dict
get_accounts_summary_dict = get_accounts_summary_instance.to_dict()
# create an instance of GetAccountsSummary from a dict
get_accounts_summary_form_dict = get_accounts_summary.from_dict(get_accounts_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


