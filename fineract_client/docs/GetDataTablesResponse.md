# GetDataTablesResponse

GetDataTablesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_table_name** | **str** |  | [optional] 
**column_header_data** | [**List[ResultsetColumnHeaderData]**](ResultsetColumnHeaderData.md) |  | [optional] 
**registered_table_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_data_tables_response import GetDataTablesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataTablesResponse from a JSON string
get_data_tables_response_instance = GetDataTablesResponse.from_json(json)
# print the JSON string representation of the object
print(GetDataTablesResponse.to_json())

# convert the object into a dict
get_data_tables_response_dict = get_data_tables_response_instance.to_dict()
# create an instance of GetDataTablesResponse from a dict
get_data_tables_response_from_dict = GetDataTablesResponse.from_dict(get_data_tables_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


