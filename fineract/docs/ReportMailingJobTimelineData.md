# ReportMailingJobTimelineData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_firstname** | **str** |  | [optional] 
**created_by_lastname** | **str** |  | [optional] 
**created_by_username** | **str** |  | [optional] 
**created_on_date** | **date** |  | [optional] 
**updated_by_firstname** | **str** |  | [optional] 
**updated_by_lastname** | **str** |  | [optional] 
**updated_by_username** | **str** |  | [optional] 
**updated_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.report_mailing_job_timeline_data import ReportMailingJobTimelineData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportMailingJobTimelineData from a JSON string
report_mailing_job_timeline_data_instance = ReportMailingJobTimelineData.from_json(json)
# print the JSON string representation of the object
print ReportMailingJobTimelineData.to_json()

# convert the object into a dict
report_mailing_job_timeline_data_dict = report_mailing_job_timeline_data_instance.to_dict()
# create an instance of ReportMailingJobTimelineData from a dict
report_mailing_job_timeline_data_form_dict = report_mailing_job_timeline_data.from_dict(report_mailing_job_timeline_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


