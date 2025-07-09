# PostAccountsTypeRequest

PostAccountsTypeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_dividend_calculation_for_inactive_clients** | **bool** |  | [optional] 
**application_date** | **str** |  | [optional] 
**charges** | [**List[PostAccountsCharges]**](PostAccountsCharges.md) |  | [optional] 
**client_id** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**lockin_period_frequency** | **int** |  | [optional] 
**lockin_period_frequency_type** | **int** |  | [optional] 
**minimum_active_period** | **int** |  | [optional] 
**minimum_active_period_frequency_type** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**requested_shares** | **int** |  | [optional] 
**savings_account_id** | **int** |  | [optional] 
**submitted_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_accounts_type_request import PostAccountsTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountsTypeRequest from a JSON string
post_accounts_type_request_instance = PostAccountsTypeRequest.from_json(json)
# print the JSON string representation of the object
print(PostAccountsTypeRequest.to_json())

# convert the object into a dict
post_accounts_type_request_dict = post_accounts_type_request_instance.to_dict()
# create an instance of PostAccountsTypeRequest from a dict
post_accounts_type_request_from_dict = PostAccountsTypeRequest.from_dict(post_accounts_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


