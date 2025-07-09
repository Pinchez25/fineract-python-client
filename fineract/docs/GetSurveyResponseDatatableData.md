# GetSurveyResponseDatatableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_table_name** | **str** |  | [optional] 
**column_header_data** | [**List[ResultsetColumnHeaderData]**](ResultsetColumnHeaderData.md) |  | [optional] 
**registered_table_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_survey_response_datatable_data import GetSurveyResponseDatatableData

# TODO update the JSON string below
json = "{}"
# create an instance of GetSurveyResponseDatatableData from a JSON string
get_survey_response_datatable_data_instance = GetSurveyResponseDatatableData.from_json(json)
# print the JSON string representation of the object
print GetSurveyResponseDatatableData.to_json()

# convert the object into a dict
get_survey_response_datatable_data_dict = get_survey_response_datatable_data_instance.to_dict()
# create an instance of GetSurveyResponseDatatableData from a dict
get_survey_response_datatable_data_form_dict = get_survey_response_datatable_data.from_dict(get_survey_response_datatable_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


