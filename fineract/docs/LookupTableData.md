# LookupTableData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entries** | [**List[LookupTableEntry]**](LookupTableEntry.md) |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.lookup_table_data import LookupTableData

# TODO update the JSON string below
json = "{}"
# create an instance of LookupTableData from a JSON string
lookup_table_data_instance = LookupTableData.from_json(json)
# print the JSON string representation of the object
print LookupTableData.to_json()

# convert the object into a dict
lookup_table_data_dict = lookup_table_data_instance.to_dict()
# create an instance of LookupTableData from a dict
lookup_table_data_form_dict = lookup_table_data.from_dict(lookup_table_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


