# PostAccountTransfersRequest

PostAccountTransfersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**from_account_id** | **int** |  | [optional] 
**from_account_type** | **int** |  | [optional] 
**from_client_id** | **int** |  | [optional] 
**from_office_id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**to_account_id** | **int** |  | [optional] 
**to_account_type** | **int** |  | [optional] 
**to_client_id** | **int** |  | [optional] 
**to_office_id** | **int** |  | [optional] 
**transfer_amount** | **float** |  | [optional] 
**transfer_date** | **str** |  | [optional] 
**transfer_description** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_account_transfers_request import PostAccountTransfersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountTransfersRequest from a JSON string
post_account_transfers_request_instance = PostAccountTransfersRequest.from_json(json)
# print the JSON string representation of the object
print(PostAccountTransfersRequest.to_json())

# convert the object into a dict
post_account_transfers_request_dict = post_account_transfers_request_instance.to_dict()
# create an instance of PostAccountTransfersRequest from a dict
post_account_transfers_request_from_dict = PostAccountTransfersRequest.from_dict(post_account_transfers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


