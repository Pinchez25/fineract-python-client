# PostRecurringDepositAccountsRequest

PostRecurringDepositAccountsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**deposit_amount** | **float** |  | [optional] 
**deposit_period** | **int** |  | [optional] 
**deposit_period_frequency_id** | **int** |  | [optional] 
**is_calendar_inherited** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**mandatory_recommended_deposit_amount** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**recurring_frequency** | **int** |  | [optional] 
**recurring_frequency_type** | **int** |  | [optional] 
**submitted_on_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_recurring_deposit_accounts_request import PostRecurringDepositAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRecurringDepositAccountsRequest from a JSON string
post_recurring_deposit_accounts_request_instance = PostRecurringDepositAccountsRequest.from_json(json)
# print the JSON string representation of the object
print(PostRecurringDepositAccountsRequest.to_json())

# convert the object into a dict
post_recurring_deposit_accounts_request_dict = post_recurring_deposit_accounts_request_instance.to_dict()
# create an instance of PostRecurringDepositAccountsRequest from a dict
post_recurring_deposit_accounts_request_from_dict = PostRecurringDepositAccountsRequest.from_dict(post_recurring_deposit_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


