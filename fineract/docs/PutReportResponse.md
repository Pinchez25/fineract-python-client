# PutReportResponse

PutReportResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutReportResponseChanges**](PutReportResponseChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_report_response import PutReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutReportResponse from a JSON string
put_report_response_instance = PutReportResponse.from_json(json)
# print the JSON string representation of the object
print(PutReportResponse.to_json())

# convert the object into a dict
put_report_response_dict = put_report_response_instance.to_dict()
# create an instance of PutReportResponse from a dict
put_report_response_from_dict = PutReportResponse.from_dict(put_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


