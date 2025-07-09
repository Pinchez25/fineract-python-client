# DeleteDataTablesResponse

DeleteDataTablesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_identifier** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.delete_data_tables_response import DeleteDataTablesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDataTablesResponse from a JSON string
delete_data_tables_response_instance = DeleteDataTablesResponse.from_json(json)
# print the JSON string representation of the object
print DeleteDataTablesResponse.to_json()

# convert the object into a dict
delete_data_tables_response_dict = delete_data_tables_response_instance.to_dict()
# create an instance of DeleteDataTablesResponse from a dict
delete_data_tables_response_form_dict = delete_data_tables_response.from_dict(delete_data_tables_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


