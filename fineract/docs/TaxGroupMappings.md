# TaxGroupMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **int** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**end_date** | **date** |  | [optional] 
**id** | **int** |  | [optional] 
**last_modified_by** | **int** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**new** | **bool** |  | [optional] 
**tax_component** | [**TaxComponent**](TaxComponent.md) |  | [optional] 
**tax_group** | [**TaxGroup**](TaxGroup.md) |  | [optional] 

## Example

```python
from fineract_client.models.tax_group_mappings import TaxGroupMappings

# TODO update the JSON string below
json = "{}"
# create an instance of TaxGroupMappings from a JSON string
tax_group_mappings_instance = TaxGroupMappings.from_json(json)
# print the JSON string representation of the object
print(TaxGroupMappings.to_json())

# convert the object into a dict
tax_group_mappings_dict = tax_group_mappings_instance.to_dict()
# create an instance of TaxGroupMappings from a dict
tax_group_mappings_from_dict = TaxGroupMappings.from_dict(tax_group_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


