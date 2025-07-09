# ReportMailingJobRunHistoryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date_time** | **datetime** |  | [optional] 
**error_log** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**report_mailing_job_id** | **int** |  | [optional] 
**start_date_time** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.report_mailing_job_run_history_data import ReportMailingJobRunHistoryData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportMailingJobRunHistoryData from a JSON string
report_mailing_job_run_history_data_instance = ReportMailingJobRunHistoryData.from_json(json)
# print the JSON string representation of the object
print(ReportMailingJobRunHistoryData.to_json())

# convert the object into a dict
report_mailing_job_run_history_data_dict = report_mailing_job_run_history_data_instance.to_dict()
# create an instance of ReportMailingJobRunHistoryData from a dict
report_mailing_job_run_history_data_from_dict = ReportMailingJobRunHistoryData.from_dict(report_mailing_job_run_history_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


