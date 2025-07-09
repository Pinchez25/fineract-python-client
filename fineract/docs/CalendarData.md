# CalendarData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_instance_id** | **int** |  | [optional] 
**calendar_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**center_id** | **str** |  | [optional] 
**created_by_user_id** | **int** |  | [optional] 
**created_by_username** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**date_format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**end_date** | **date** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**entity_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**entity_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**first_reminder** | **int** |  | [optional] 
**frequency** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**frequency_nth_day_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**frequency_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**human_readable** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interval** | **int** |  | [optional] 
**last_updated_by_user_id** | **int** |  | [optional] 
**last_updated_by_username** | **str** |  | [optional] 
**last_updated_date** | **datetime** |  | [optional] 
**locale** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**meeting_time** | [**LocalTime**](LocalTime.md) |  | [optional] 
**next_ten_recurring_dates** | **List[date]** |  | [optional] 
**recent_eligible_meeting_date** | **date** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**recurring_dates** | **List[date]** |  | [optional] 
**remind_by** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**remind_by_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**repeating** | **bool** |  | [optional] 
**repeats_on_day** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**repeats_on_day_of_month** | **int** |  | [optional] 
**repeats_on_day_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**repeats_on_nth_day_of_month** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**row_index** | **int** |  | [optional] 
**second_reminder** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**type_id** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.calendar_data import CalendarData

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarData from a JSON string
calendar_data_instance = CalendarData.from_json(json)
# print the JSON string representation of the object
print CalendarData.to_json()

# convert the object into a dict
calendar_data_dict = calendar_data_instance.to_dict()
# create an instance of CalendarData from a dict
calendar_data_form_dict = calendar_data.from_dict(calendar_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


