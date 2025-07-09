# PostFixedDepositAccountsResponse

PostFixedDepositAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_fixed_deposit_accounts_response import PostFixedDepositAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostFixedDepositAccountsResponse from a JSON string
post_fixed_deposit_accounts_response_instance = PostFixedDepositAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(PostFixedDepositAccountsResponse.to_json())

# convert the object into a dict
post_fixed_deposit_accounts_response_dict = post_fixed_deposit_accounts_response_instance.to_dict()
# create an instance of PostFixedDepositAccountsResponse from a dict
post_fixed_deposit_accounts_response_from_dict = PostFixedDepositAccountsResponse.from_dict(post_fixed_deposit_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


