# PostInitiateTransferRequest

PostInitiateTransferRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**owner_external_id** | **str** |  | [optional] 
**purchase_price_ratio** | **str** |  | [optional] 
**settlement_date** | **str** |  | [optional] 
**transfer_external_id** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_initiate_transfer_request import PostInitiateTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostInitiateTransferRequest from a JSON string
post_initiate_transfer_request_instance = PostInitiateTransferRequest.from_json(json)
# print the JSON string representation of the object
print(PostInitiateTransferRequest.to_json())

# convert the object into a dict
post_initiate_transfer_request_dict = post_initiate_transfer_request_instance.to_dict()
# create an instance of PostInitiateTransferRequest from a dict
post_initiate_transfer_request_from_dict = PostInitiateTransferRequest.from_dict(post_initiate_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


