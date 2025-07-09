# GetCentersPageItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**status** | [**GetCentersStatus**](GetCentersStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_page_items import GetCentersPageItems

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersPageItems from a JSON string
get_centers_page_items_instance = GetCentersPageItems.from_json(json)
# print the JSON string representation of the object
print(GetCentersPageItems.to_json())

# convert the object into a dict
get_centers_page_items_dict = get_centers_page_items_instance.to_dict()
# create an instance of GetCentersPageItems from a dict
get_centers_page_items_from_dict = GetCentersPageItems.from_dict(get_centers_page_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


