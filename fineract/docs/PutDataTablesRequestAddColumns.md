# PutDataTablesRequestAddColumns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**indexed** | **bool** | Defaults to false | [optional] 
**mandatory** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**unique** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.put_data_tables_request_add_columns import PutDataTablesRequestAddColumns

# TODO update the JSON string below
json = "{}"
# create an instance of PutDataTablesRequestAddColumns from a JSON string
put_data_tables_request_add_columns_instance = PutDataTablesRequestAddColumns.from_json(json)
# print the JSON string representation of the object
print PutDataTablesRequestAddColumns.to_json()

# convert the object into a dict
put_data_tables_request_add_columns_dict = put_data_tables_request_add_columns_instance.to_dict()
# create an instance of PutDataTablesRequestAddColumns from a dict
put_data_tables_request_add_columns_form_dict = put_data_tables_request_add_columns.from_dict(put_data_tables_request_add_columns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


