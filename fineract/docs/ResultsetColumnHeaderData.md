# ResultsetColumnHeaderData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolean_display_type** | **bool** |  | [optional] 
**code_lookup_display_type** | **bool** |  | [optional] 
**code_value_display_type** | **bool** |  | [optional] 
**column_code** | **str** |  | [optional] 
**column_display_type** | **str** |  | [optional] 
**column_length** | **int** |  | [optional] 
**column_name** | **str** |  | [optional] 
**column_type** | **str** |  | [optional] 
**column_values** | **List[object]** |  | [optional] 
**date_display_type** | **bool** |  | [optional] 
**date_time_display_type** | **bool** |  | [optional] 
**decimal_display_type** | **bool** |  | [optional] 
**integer_display_type** | **bool** |  | [optional] 
**is_column_indexed** | **bool** |  | [optional] 
**is_column_nullable** | **bool** |  | [optional] 
**is_column_primary_key** | **bool** |  | [optional] 
**is_column_unique** | **bool** |  | [optional] 
**mandatory** | **bool** |  | [optional] 
**string_display_type** | **bool** |  | [optional] 
**text_display_type** | **bool** |  | [optional] 
**time_display_type** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.resultset_column_header_data import ResultsetColumnHeaderData

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsetColumnHeaderData from a JSON string
resultset_column_header_data_instance = ResultsetColumnHeaderData.from_json(json)
# print the JSON string representation of the object
print(ResultsetColumnHeaderData.to_json())

# convert the object into a dict
resultset_column_header_data_dict = resultset_column_header_data_instance.to_dict()
# create an instance of ResultsetColumnHeaderData from a dict
resultset_column_header_data_from_dict = ResultsetColumnHeaderData.from_dict(resultset_column_header_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


