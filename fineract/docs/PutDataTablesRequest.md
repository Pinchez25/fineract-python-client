# PutDataTablesRequest

PutDataTablesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_columns** | [**List[PutDataTablesRequestAddColumns]**](PutDataTablesRequestAddColumns.md) |  | [optional] 
**apptable_name** | **str** |  | [optional] 
**change_columns** | [**List[PutDataTablesRequestChangeColumns]**](PutDataTablesRequestChangeColumns.md) |  | [optional] 
**drop_columns** | [**List[PutDataTablesRequestDropColumns]**](PutDataTablesRequestDropColumns.md) |  | [optional] 

## Example

```python
from fineract_client.models.put_data_tables_request import PutDataTablesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutDataTablesRequest from a JSON string
put_data_tables_request_instance = PutDataTablesRequest.from_json(json)
# print the JSON string representation of the object
print PutDataTablesRequest.to_json()

# convert the object into a dict
put_data_tables_request_dict = put_data_tables_request_instance.to_dict()
# create an instance of PutDataTablesRequest from a dict
put_data_tables_request_form_dict = put_data_tables_request.from_dict(put_data_tables_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


