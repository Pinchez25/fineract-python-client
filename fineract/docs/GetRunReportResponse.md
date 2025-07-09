# GetRunReportResponse

GetRunReportResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_headers** | [**List[GetRunReportColumnHeaders]**](GetRunReportColumnHeaders.md) |  | [optional] 
**data** | [**List[GetPocketData]**](GetPocketData.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_run_report_response import GetRunReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRunReportResponse from a JSON string
get_run_report_response_instance = GetRunReportResponse.from_json(json)
# print the JSON string representation of the object
print(GetRunReportResponse.to_json())

# convert the object into a dict
get_run_report_response_dict = get_run_report_response_instance.to_dict()
# create an instance of GetRunReportResponse from a dict
get_run_report_response_from_dict = GetRunReportResponse.from_dict(get_run_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


