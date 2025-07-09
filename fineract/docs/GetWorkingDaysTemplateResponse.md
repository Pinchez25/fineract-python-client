# GetWorkingDaysTemplateResponse

GetWorkingDaysTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repayment_reschedule_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_working_days_template_response import GetWorkingDaysTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWorkingDaysTemplateResponse from a JSON string
get_working_days_template_response_instance = GetWorkingDaysTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(GetWorkingDaysTemplateResponse.to_json())

# convert the object into a dict
get_working_days_template_response_dict = get_working_days_template_response_instance.to_dict()
# create an instance of GetWorkingDaysTemplateResponse from a dict
get_working_days_template_response_from_dict = GetWorkingDaysTemplateResponse.from_dict(get_working_days_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


