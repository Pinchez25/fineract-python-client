# PutDataTablesRequestChangeColumns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**indexed** | **bool** | Defaults to false | [optional] 
**mandatory** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**new_code** | **str** |  | [optional] 
**new_name** | **str** |  | [optional] 
**unique** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.put_data_tables_request_change_columns import PutDataTablesRequestChangeColumns

# TODO update the JSON string below
json = "{}"
# create an instance of PutDataTablesRequestChangeColumns from a JSON string
put_data_tables_request_change_columns_instance = PutDataTablesRequestChangeColumns.from_json(json)
# print the JSON string representation of the object
print(PutDataTablesRequestChangeColumns.to_json())

# convert the object into a dict
put_data_tables_request_change_columns_dict = put_data_tables_request_change_columns_instance.to_dict()
# create an instance of PutDataTablesRequestChangeColumns from a dict
put_data_tables_request_change_columns_from_dict = PutDataTablesRequestChangeColumns.from_dict(put_data_tables_request_change_columns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


