# GetCentersStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_status import GetCentersStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersStatus from a JSON string
get_centers_status_instance = GetCentersStatus.from_json(json)
# print the JSON string representation of the object
print GetCentersStatus.to_json()

# convert the object into a dict
get_centers_status_dict = get_centers_status_instance.to_dict()
# create an instance of GetCentersStatus from a dict
get_centers_status_form_dict = get_centers_status.from_dict(get_centers_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


