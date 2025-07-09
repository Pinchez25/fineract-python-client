# PutReportRequest

PutReportRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_name** | **str** |  | [optional] 
**report_parameters** | **List[object]** |  | [optional] 

## Example

```python
from fineract_client.models.put_report_request import PutReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutReportRequest from a JSON string
put_report_request_instance = PutReportRequest.from_json(json)
# print the JSON string representation of the object
print PutReportRequest.to_json()

# convert the object into a dict
put_report_request_dict = put_report_request_instance.to_dict()
# create an instance of PutReportRequest from a dict
put_report_request_form_dict = put_report_request.from_dict(put_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


