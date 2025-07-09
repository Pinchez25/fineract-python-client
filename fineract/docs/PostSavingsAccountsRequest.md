# PostSavingsAccountsRequest

PostSavingsAccountsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**product_id** | **int** |  | [optional] 
**submitted_on_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_savings_accounts_request import PostSavingsAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSavingsAccountsRequest from a JSON string
post_savings_accounts_request_instance = PostSavingsAccountsRequest.from_json(json)
# print the JSON string representation of the object
print PostSavingsAccountsRequest.to_json()

# convert the object into a dict
post_savings_accounts_request_dict = post_savings_accounts_request_instance.to_dict()
# create an instance of PostSavingsAccountsRequest from a dict
post_savings_accounts_request_form_dict = post_savings_accounts_request.from_dict(post_savings_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


