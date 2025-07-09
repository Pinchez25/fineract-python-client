# PutWorkingDaysRequest

PutWorkingDaysRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extend_term_for_daily_repayments** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**repayment_reschedule_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.put_working_days_request import PutWorkingDaysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutWorkingDaysRequest from a JSON string
put_working_days_request_instance = PutWorkingDaysRequest.from_json(json)
# print the JSON string representation of the object
print(PutWorkingDaysRequest.to_json())

# convert the object into a dict
put_working_days_request_dict = put_working_days_request_instance.to_dict()
# create an instance of PutWorkingDaysRequest from a dict
put_working_days_request_from_dict = PutWorkingDaysRequest.from_dict(put_working_days_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


