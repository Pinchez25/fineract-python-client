# PostFixedDepositAccountsRequest

PostFixedDepositAccountsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**deposit_amount** | **float** |  | [optional] 
**deposit_period** | **int** |  | [optional] 
**deposit_period_frequency_id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**product_id** | **int** |  | [optional] 
**submitted_on_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_fixed_deposit_accounts_request import PostFixedDepositAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFixedDepositAccountsRequest from a JSON string
post_fixed_deposit_accounts_request_instance = PostFixedDepositAccountsRequest.from_json(json)
# print the JSON string representation of the object
print(PostFixedDepositAccountsRequest.to_json())

# convert the object into a dict
post_fixed_deposit_accounts_request_dict = post_fixed_deposit_accounts_request_instance.to_dict()
# create an instance of PostFixedDepositAccountsRequest from a dict
post_fixed_deposit_accounts_request_from_dict = PostFixedDepositAccountsRequest.from_dict(post_fixed_deposit_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


