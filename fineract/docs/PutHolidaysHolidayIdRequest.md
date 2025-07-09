# PutHolidaysHolidayIdRequest

PutHolidaysHolidayIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_holidays_holiday_id_request import PutHolidaysHolidayIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutHolidaysHolidayIdRequest from a JSON string
put_holidays_holiday_id_request_instance = PutHolidaysHolidayIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutHolidaysHolidayIdRequest.to_json())

# convert the object into a dict
put_holidays_holiday_id_request_dict = put_holidays_holiday_id_request_instance.to_dict()
# create an instance of PutHolidaysHolidayIdRequest from a dict
put_holidays_holiday_id_request_from_dict = PutHolidaysHolidayIdRequest.from_dict(put_holidays_holiday_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


