# GetClientsColumnHeaderData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_display_type** | **str** |  | [optional] 
**column_length** | **int** |  | [optional] 
**column_name** | **str** |  | [optional] 
**column_type** | **str** |  | [optional] 
**column_values** | **List[str]** |  | [optional] 
**is_column_nullable** | **bool** |  | [optional] 
**is_column_primary_key** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_column_header_data import GetClientsColumnHeaderData

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsColumnHeaderData from a JSON string
get_clients_column_header_data_instance = GetClientsColumnHeaderData.from_json(json)
# print the JSON string representation of the object
print GetClientsColumnHeaderData.to_json()

# convert the object into a dict
get_clients_column_header_data_dict = get_clients_column_header_data_instance.to_dict()
# create an instance of GetClientsColumnHeaderData from a dict
get_clients_column_header_data_form_dict = get_clients_column_header_data.from_dict(get_clients_column_header_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


