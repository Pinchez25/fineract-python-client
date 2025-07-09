# GetReportsResponse

GetReportsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_report** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**report_category** | **str** |  | [optional] 
**report_name** | **str** |  | [optional] 
**report_parameters** | **List[object]** |  | [optional] 
**report_sql** | **str** |  | [optional] 
**report_sub_type** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**use_report** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_reports_response import GetReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReportsResponse from a JSON string
get_reports_response_instance = GetReportsResponse.from_json(json)
# print the JSON string representation of the object
print(GetReportsResponse.to_json())

# convert the object into a dict
get_reports_response_dict = get_reports_response_instance.to_dict()
# create an instance of GetReportsResponse from a dict
get_reports_response_from_dict = GetReportsResponse.from_dict(get_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


