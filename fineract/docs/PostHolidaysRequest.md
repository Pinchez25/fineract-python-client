# PostHolidaysRequest

PostHolidaysRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**from_date** | **date** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**offices** | [**List[PostHolidaysRequestOffices]**](PostHolidaysRequestOffices.md) |  | [optional] 
**repayments_rescheduled_to** | **date** |  | [optional] 
**to_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.post_holidays_request import PostHolidaysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostHolidaysRequest from a JSON string
post_holidays_request_instance = PostHolidaysRequest.from_json(json)
# print the JSON string representation of the object
print PostHolidaysRequest.to_json()

# convert the object into a dict
post_holidays_request_dict = post_holidays_request_instance.to_dict()
# create an instance of PostHolidaysRequest from a dict
post_holidays_request_form_dict = post_holidays_request.from_dict(post_holidays_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


