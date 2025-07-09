# PutReportResponseChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_name** | **str** |  | [optional] 
**report_parameters** | **List[object]** |  | [optional] 

## Example

```python
from fineract_client.models.put_report_response_changes import PutReportResponseChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutReportResponseChanges from a JSON string
put_report_response_changes_instance = PutReportResponseChanges.from_json(json)
# print the JSON string representation of the object
print PutReportResponseChanges.to_json()

# convert the object into a dict
put_report_response_changes_dict = put_report_response_changes_instance.to_dict()
# create an instance of PutReportResponseChanges from a dict
put_report_response_changes_form_dict = put_report_response_changes.from_dict(put_report_response_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


