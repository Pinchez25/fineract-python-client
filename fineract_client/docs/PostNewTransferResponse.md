# PostNewTransferResponse

PostNewTransferResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 
**savings_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_new_transfer_response import PostNewTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostNewTransferResponse from a JSON string
post_new_transfer_response_instance = PostNewTransferResponse.from_json(json)
# print the JSON string representation of the object
print(PostNewTransferResponse.to_json())

# convert the object into a dict
post_new_transfer_response_dict = post_new_transfer_response_instance.to_dict()
# create an instance of PostNewTransferResponse from a dict
post_new_transfer_response_from_dict = PostNewTransferResponse.from_dict(post_new_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


