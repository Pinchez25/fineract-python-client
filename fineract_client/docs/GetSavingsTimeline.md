# GetSavingsTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_on_date** | **date** |  | [optional] 
**approved_by_firstname** | **str** |  | [optional] 
**approved_by_lastname** | **str** |  | [optional] 
**approved_by_username** | **str** |  | [optional] 
**approved_on_date** | **date** |  | [optional] 
**submitted_by_firstname** | **str** |  | [optional] 
**submitted_by_lastname** | **str** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_timeline import GetSavingsTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsTimeline from a JSON string
get_savings_timeline_instance = GetSavingsTimeline.from_json(json)
# print the JSON string representation of the object
print(GetSavingsTimeline.to_json())

# convert the object into a dict
get_savings_timeline_dict = get_savings_timeline_instance.to_dict()
# create an instance of GetSavingsTimeline from a dict
get_savings_timeline_from_dict = GetSavingsTimeline.from_dict(get_savings_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


