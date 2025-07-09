# PostInitiateTransferResponse

PostInitiateTransferResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**ExternalAssetOwnerTransferChangesData**](ExternalAssetOwnerTransferChangesData.md) |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**resource_external_id** | **str** | transfer external ID | [optional] 
**resource_id** | **int** | transfer ID | [optional] 
**sub_resource_external_id** | **str** | loan external ID | [optional] 
**sub_resource_id** | **int** | loan ID | [optional] 

## Example

```python
from fineract_client.models.post_initiate_transfer_response import PostInitiateTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostInitiateTransferResponse from a JSON string
post_initiate_transfer_response_instance = PostInitiateTransferResponse.from_json(json)
# print the JSON string representation of the object
print(PostInitiateTransferResponse.to_json())

# convert the object into a dict
post_initiate_transfer_response_dict = post_initiate_transfer_response_instance.to_dict()
# create an instance of PostInitiateTransferResponse from a dict
post_initiate_transfer_response_from_dict = PostInitiateTransferResponse.from_dict(post_initiate_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


