# PutDataTablesResponse

PutDataTablesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_identifier** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_data_tables_response import PutDataTablesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutDataTablesResponse from a JSON string
put_data_tables_response_instance = PutDataTablesResponse.from_json(json)
# print the JSON string representation of the object
print PutDataTablesResponse.to_json()

# convert the object into a dict
put_data_tables_response_dict = put_data_tables_response_instance.to_dict()
# create an instance of PutDataTablesResponse from a dict
put_data_tables_response_form_dict = put_data_tables_response.from_dict(put_data_tables_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


