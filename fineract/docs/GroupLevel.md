# GroupLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**center** | **bool** |  | [optional] 
**group** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**level_name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**recursable** | **bool** |  | [optional] 
**super_parent** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.group_level import GroupLevel

# TODO update the JSON string below
json = "{}"
# create an instance of GroupLevel from a JSON string
group_level_instance = GroupLevel.from_json(json)
# print the JSON string representation of the object
print(GroupLevel.to_json())

# convert the object into a dict
group_level_dict = group_level_instance.to_dict()
# create an instance of GroupLevel from a dict
group_level_from_dict = GroupLevel.from_dict(group_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


