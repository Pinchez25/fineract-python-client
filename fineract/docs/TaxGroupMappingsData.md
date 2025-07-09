# TaxGroupMappingsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_component** | [**TaxComponentData**](TaxComponentData.md) |  | [optional] 

## Example

```python
from fineract_client.models.tax_group_mappings_data import TaxGroupMappingsData

# TODO update the JSON string below
json = "{}"
# create an instance of TaxGroupMappingsData from a JSON string
tax_group_mappings_data_instance = TaxGroupMappingsData.from_json(json)
# print the JSON string representation of the object
print TaxGroupMappingsData.to_json()

# convert the object into a dict
tax_group_mappings_data_dict = tax_group_mappings_data_instance.to_dict()
# create an instance of TaxGroupMappingsData from a dict
tax_group_mappings_data_form_dict = tax_group_mappings_data.from_dict(tax_group_mappings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


