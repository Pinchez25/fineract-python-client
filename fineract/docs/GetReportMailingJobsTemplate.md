# GetReportMailingJobsTemplate

GetReportMailingJobsTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_attachment_file_format_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**is_active** | **bool** |  | [optional] 
**stretchy_report_param_date_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_report_mailing_jobs_template import GetReportMailingJobsTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of GetReportMailingJobsTemplate from a JSON string
get_report_mailing_jobs_template_instance = GetReportMailingJobsTemplate.from_json(json)
# print the JSON string representation of the object
print(GetReportMailingJobsTemplate.to_json())

# convert the object into a dict
get_report_mailing_jobs_template_dict = get_report_mailing_jobs_template_instance.to_dict()
# create an instance of GetReportMailingJobsTemplate from a dict
get_report_mailing_jobs_template_from_dict = GetReportMailingJobsTemplate.from_dict(get_report_mailing_jobs_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


