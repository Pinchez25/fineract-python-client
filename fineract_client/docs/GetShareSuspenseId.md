# GetShareSuspenseId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_share_suspense_id import GetShareSuspenseId

# TODO update the JSON string below
json = "{}"
# create an instance of GetShareSuspenseId from a JSON string
get_share_suspense_id_instance = GetShareSuspenseId.from_json(json)
# print the JSON string representation of the object
print(GetShareSuspenseId.to_json())

# convert the object into a dict
get_share_suspense_id_dict = get_share_suspense_id_instance.to_dict()
# create an instance of GetShareSuspenseId from a dict
get_share_suspense_id_from_dict = GetShareSuspenseId.from_dict(get_share_suspense_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


