# PutGroupsGroupIdResponse

PutGroupsGroupIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutGroupsGroupIdChanges**](PutGroupsGroupIdChanges.md) |  | [optional] 
**group_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_groups_group_id_response import PutGroupsGroupIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutGroupsGroupIdResponse from a JSON string
put_groups_group_id_response_instance = PutGroupsGroupIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutGroupsGroupIdResponse.to_json())

# convert the object into a dict
put_groups_group_id_response_dict = put_groups_group_id_response_instance.to_dict()
# create an instance of PutGroupsGroupIdResponse from a dict
put_groups_group_id_response_from_dict = PutGroupsGroupIdResponse.from_dict(put_groups_group_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


