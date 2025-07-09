# PostCollectionSheetResponse

PostCollectionSheetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PostCollectionSheetChanges**](PostCollectionSheetChanges.md) |  | [optional] 
**group_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_collection_sheet_response import PostCollectionSheetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCollectionSheetResponse from a JSON string
post_collection_sheet_response_instance = PostCollectionSheetResponse.from_json(json)
# print the JSON string representation of the object
print(PostCollectionSheetResponse.to_json())

# convert the object into a dict
post_collection_sheet_response_dict = post_collection_sheet_response_instance.to_dict()
# create an instance of PostCollectionSheetResponse from a dict
post_collection_sheet_response_from_dict = PostCollectionSheetResponse.from_dict(post_collection_sheet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


