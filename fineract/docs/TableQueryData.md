# TableQueryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**AdvancedQueryData**](AdvancedQueryData.md) |  | [optional] 
**table** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.table_query_data import TableQueryData

# TODO update the JSON string below
json = "{}"
# create an instance of TableQueryData from a JSON string
table_query_data_instance = TableQueryData.from_json(json)
# print the JSON string representation of the object
print TableQueryData.to_json()

# convert the object into a dict
table_query_data_dict = table_query_data_instance.to_dict()
# create an instance of TableQueryData from a dict
table_query_data_form_dict = table_query_data.from_dict(table_query_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


