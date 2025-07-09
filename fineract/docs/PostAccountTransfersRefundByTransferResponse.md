# PostAccountTransfersRefundByTransferResponse

PostAccountTransfersRefundByTransferResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_account_transfers_refund_by_transfer_response import PostAccountTransfersRefundByTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountTransfersRefundByTransferResponse from a JSON string
post_account_transfers_refund_by_transfer_response_instance = PostAccountTransfersRefundByTransferResponse.from_json(json)
# print the JSON string representation of the object
print(PostAccountTransfersRefundByTransferResponse.to_json())

# convert the object into a dict
post_account_transfers_refund_by_transfer_response_dict = post_account_transfers_refund_by_transfer_response_instance.to_dict()
# create an instance of PostAccountTransfersRefundByTransferResponse from a dict
post_account_transfers_refund_by_transfer_response_from_dict = PostAccountTransfersRefundByTransferResponse.from_dict(post_account_transfers_refund_by_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


