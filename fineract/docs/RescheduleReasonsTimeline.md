# RescheduleReasonsTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from fineract_client.models.reschedule_reasons_timeline import RescheduleReasonsTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of RescheduleReasonsTimeline from a JSON string
reschedule_reasons_timeline_instance = RescheduleReasonsTimeline.from_json(json)
# print the JSON string representation of the object
print RescheduleReasonsTimeline.to_json()

# convert the object into a dict
reschedule_reasons_timeline_dict = reschedule_reasons_timeline_instance.to_dict()
# create an instance of RescheduleReasonsTimeline from a dict
reschedule_reasons_timeline_form_dict = reschedule_reasons_timeline.from_dict(reschedule_reasons_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


