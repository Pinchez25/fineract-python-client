# GetHolidaysResponse

GetHolidaysResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**repayments_rescheduled_to** | **date** |  | [optional] 
**status** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**to_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.get_holidays_response import GetHolidaysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHolidaysResponse from a JSON string
get_holidays_response_instance = GetHolidaysResponse.from_json(json)
# print the JSON string representation of the object
print GetHolidaysResponse.to_json()

# convert the object into a dict
get_holidays_response_dict = get_holidays_response_instance.to_dict()
# create an instance of GetHolidaysResponse from a dict
get_holidays_response_form_dict = get_holidays_response.from_dict(get_holidays_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


