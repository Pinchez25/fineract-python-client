# GetReportsTemplateResponse

GetReportsTemplateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_parameters** | **List[object]** |  | [optional] 
**allowed_report_sub_types** | **List[str]** |  | [optional] 
**allowed_report_types** | **List[str]** |  | [optional] 

## Example

```python
from fineract_client.models.get_reports_template_response import GetReportsTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReportsTemplateResponse from a JSON string
get_reports_template_response_instance = GetReportsTemplateResponse.from_json(json)
# print the JSON string representation of the object
print GetReportsTemplateResponse.to_json()

# convert the object into a dict
get_reports_template_response_dict = get_reports_template_response_instance.to_dict()
# create an instance of GetReportsTemplateResponse from a dict
get_reports_template_response_form_dict = get_reports_template_response.from_dict(get_reports_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


