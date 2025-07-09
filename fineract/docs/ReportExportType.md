# ReportExportType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**query_parameter** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.report_export_type import ReportExportType

# TODO update the JSON string below
json = "{}"
# create an instance of ReportExportType from a JSON string
report_export_type_instance = ReportExportType.from_json(json)
# print the JSON string representation of the object
print ReportExportType.to_json()

# convert the object into a dict
report_export_type_dict = report_export_type_instance.to_dict()
# create an instance of ReportExportType from a dict
report_export_type_form_dict = report_export_type.from_dict(report_export_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


