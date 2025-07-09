# GetRescheduleReasonsTemplateResponse

GetRescheduleReasonsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reschedule_reasons** | [**List[GetRescheduleReasonsAllowedTypes]**](GetRescheduleReasonsAllowedTypes.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_reschedule_reasons_template_response import GetRescheduleReasonsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRescheduleReasonsTemplateResponse from a JSON string
get_reschedule_reasons_template_response_instance = GetRescheduleReasonsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetRescheduleReasonsTemplateResponse.to_json()

# convert the object into a dict
get_reschedule_reasons_template_response_dict = get_reschedule_reasons_template_response_instance.to_dict()
# create an instance of GetRescheduleReasonsTemplateResponse from a dict
get_reschedule_reasons_template_response_form_dict = get_reschedule_reasons_template_response.from_dict(get_reschedule_reasons_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


