# RunReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_headers** | [**List[ResultsetColumnHeaderData]**](ResultsetColumnHeaderData.md) |  | [optional] 
**data** | [**List[ResultsetRowData]**](ResultsetRowData.md) |  | [optional] 

## Example

```python
from fineract_client.models.run_reports_response import RunReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunReportsResponse from a JSON string
run_reports_response_instance = RunReportsResponse.from_json(json)
# print the JSON string representation of the object
print RunReportsResponse.to_json()

# convert the object into a dict
run_reports_response_dict = run_reports_response_instance.to_dict()
# create an instance of RunReportsResponse from a dict
run_reports_response_form_dict = run_reports_response.from_dict(run_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


