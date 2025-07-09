# PostSavingsAccountTransactionsRequest

PostSavingsAccountTransactionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**lien_allowed** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**payment_type_id** | **int** |  | [optional] 
**reason_for_block** | **str** |  | [optional] 
**transaction_amount** | **float** |  | [optional] 
**transaction_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_savings_account_transactions_request import PostSavingsAccountTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSavingsAccountTransactionsRequest from a JSON string
post_savings_account_transactions_request_instance = PostSavingsAccountTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print PostSavingsAccountTransactionsRequest.to_json()

# convert the object into a dict
post_savings_account_transactions_request_dict = post_savings_account_transactions_request_instance.to_dict()
# create an instance of PostSavingsAccountTransactionsRequest from a dict
post_savings_account_transactions_request_form_dict = post_savings_account_transactions_request.from_dict(post_savings_account_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


