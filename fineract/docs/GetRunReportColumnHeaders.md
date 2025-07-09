# GetRunReportColumnHeaders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_name** | **str** |  | [optional] 
**column_type** | **str** |  | [optional] 
**column_values** | **str** |  | [optional] 
**is_column_nullable** | **bool** |  | [optional] 
**is_column_primary_key** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_run_report_column_headers import GetRunReportColumnHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of GetRunReportColumnHeaders from a JSON string
get_run_report_column_headers_instance = GetRunReportColumnHeaders.from_json(json)
# print the JSON string representation of the object
print GetRunReportColumnHeaders.to_json()

# convert the object into a dict
get_run_report_column_headers_dict = get_run_report_column_headers_instance.to_dict()
# create an instance of GetRunReportColumnHeaders from a dict
get_run_report_column_headers_form_dict = get_run_report_column_headers.from_dict(get_run_report_column_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


