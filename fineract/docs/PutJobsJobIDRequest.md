# PutJobsJobIDRequest

PutJobsJobsIDRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**cron_expression** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_jobs_job_id_request import PutJobsJobIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutJobsJobIDRequest from a JSON string
put_jobs_job_id_request_instance = PutJobsJobIDRequest.from_json(json)
# print the JSON string representation of the object
print PutJobsJobIDRequest.to_json()

# convert the object into a dict
put_jobs_job_id_request_dict = put_jobs_job_id_request_instance.to_dict()
# create an instance of PutJobsJobIDRequest from a dict
put_jobs_job_id_request_form_dict = put_jobs_job_id_request.from_dict(put_jobs_job_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


