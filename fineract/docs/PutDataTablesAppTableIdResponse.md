# PutDataTablesAppTableIdResponse

PutDataTablesAppTableIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **Dict[str, object]** |  | [optional] 
**client_id** | **int** |  | [optional] 
**loan_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_data_tables_app_table_id_response import PutDataTablesAppTableIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutDataTablesAppTableIdResponse from a JSON string
put_data_tables_app_table_id_response_instance = PutDataTablesAppTableIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutDataTablesAppTableIdResponse.to_json())

# convert the object into a dict
put_data_tables_app_table_id_response_dict = put_data_tables_app_table_id_response_instance.to_dict()
# create an instance of PutDataTablesAppTableIdResponse from a dict
put_data_tables_app_table_id_response_from_dict = PutDataTablesAppTableIdResponse.from_dict(put_data_tables_app_table_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


