# GetGroupsPageItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**status** | [**GetGroupsStatus**](GetGroupsStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_groups_page_items import GetGroupsPageItems

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupsPageItems from a JSON string
get_groups_page_items_instance = GetGroupsPageItems.from_json(json)
# print the JSON string representation of the object
print GetGroupsPageItems.to_json()

# convert the object into a dict
get_groups_page_items_dict = get_groups_page_items_instance.to_dict()
# create an instance of GetGroupsPageItems from a dict
get_groups_page_items_form_dict = get_groups_page_items.from_dict(get_groups_page_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


