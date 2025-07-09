# PostCollectionSheetChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**savings_transactions** | **List[int]** |  | [optional] 
**date_format** | **str** |  | [optional] 
**loan_transactions** | **List[int]** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_collection_sheet_changes import PostCollectionSheetChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PostCollectionSheetChanges from a JSON string
post_collection_sheet_changes_instance = PostCollectionSheetChanges.from_json(json)
# print the JSON string representation of the object
print(PostCollectionSheetChanges.to_json())

# convert the object into a dict
post_collection_sheet_changes_dict = post_collection_sheet_changes_instance.to_dict()
# create an instance of PostCollectionSheetChanges from a dict
post_collection_sheet_changes_from_dict = PostCollectionSheetChanges.from_dict(post_collection_sheet_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


