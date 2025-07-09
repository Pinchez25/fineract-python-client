# PutGroupsGroupIdRequest

PutGroupsGroupIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_groups_group_id_request import PutGroupsGroupIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutGroupsGroupIdRequest from a JSON string
put_groups_group_id_request_instance = PutGroupsGroupIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutGroupsGroupIdRequest.to_json())

# convert the object into a dict
put_groups_group_id_request_dict = put_groups_group_id_request_instance.to_dict()
# create an instance of PutGroupsGroupIdRequest from a dict
put_groups_group_id_request_from_dict = PutGroupsGroupIdRequest.from_dict(put_groups_group_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


