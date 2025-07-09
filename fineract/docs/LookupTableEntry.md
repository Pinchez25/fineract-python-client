# LookupTableEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** |  | [optional] 
**value_from** | **int** |  | [optional] 
**value_to** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.lookup_table_entry import LookupTableEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LookupTableEntry from a JSON string
lookup_table_entry_instance = LookupTableEntry.from_json(json)
# print the JSON string representation of the object
print(LookupTableEntry.to_json())

# convert the object into a dict
lookup_table_entry_dict = lookup_table_entry_instance.to_dict()
# create an instance of LookupTableEntry from a dict
lookup_table_entry_from_dict = LookupTableEntry.from_dict(lookup_table_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


