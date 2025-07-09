# GetWorkingDaysResponse

GetWorkingDaysResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extend_term_for_daily_repayments** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**repayment_reschedule_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_working_days_response import GetWorkingDaysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkingDaysResponse from a JSON string
get_working_days_response_instance = GetWorkingDaysResponse.from_json(json)
# print the JSON string representation of the object
print GetWorkingDaysResponse.to_json()

# convert the object into a dict
get_working_days_response_dict = get_working_days_response_instance.to_dict()
# create an instance of GetWorkingDaysResponse from a dict
get_working_days_response_form_dict = get_working_days_response.from_dict(get_working_days_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


