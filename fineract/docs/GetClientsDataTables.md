# GetClientsDataTables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_table_name** | **str** |  | [optional] 
**column_header_data** | [**List[GetClientsColumnHeaderData]**](GetClientsColumnHeaderData.md) |  | [optional] 
**registered_table_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_data_tables import GetClientsDataTables

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsDataTables from a JSON string
get_clients_data_tables_instance = GetClientsDataTables.from_json(json)
# print the JSON string representation of the object
print(GetClientsDataTables.to_json())

# convert the object into a dict
get_clients_data_tables_dict = get_clients_data_tables_instance.to_dict()
# create an instance of GetClientsDataTables from a dict
get_clients_data_tables_from_dict = GetClientsDataTables.from_dict(get_clients_data_tables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


