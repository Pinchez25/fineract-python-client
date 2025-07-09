# GetCentersTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submitted_by_firstname** | **str** |  | [optional] 
**submitted_by_lastname** | **str** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_timeline import GetCentersTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersTimeline from a JSON string
get_centers_timeline_instance = GetCentersTimeline.from_json(json)
# print the JSON string representation of the object
print(GetCentersTimeline.to_json())

# convert the object into a dict
get_centers_timeline_dict = get_centers_timeline_instance.to_dict()
# create an instance of GetCentersTimeline from a dict
get_centers_timeline_from_dict = GetCentersTimeline.from_dict(get_centers_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


