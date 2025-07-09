# PutHolidaysHolidayIdResponse

PutHolidaysHolidayIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutHolidaysHolidayIdResponseChanges**](PutHolidaysHolidayIdResponseChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_holidays_holiday_id_response import PutHolidaysHolidayIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutHolidaysHolidayIdResponse from a JSON string
put_holidays_holiday_id_response_instance = PutHolidaysHolidayIdResponse.from_json(json)
# print the JSON string representation of the object
print PutHolidaysHolidayIdResponse.to_json()

# convert the object into a dict
put_holidays_holiday_id_response_dict = put_holidays_holiday_id_response_instance.to_dict()
# create an instance of PutHolidaysHolidayIdResponse from a dict
put_holidays_holiday_id_response_form_dict = put_holidays_holiday_id_response.from_dict(put_holidays_holiday_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


