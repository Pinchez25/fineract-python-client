# GetTaxesGroupTaxAssociations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 
**tax_component** | [**GetTaxesGroupTaxComponent**](GetTaxesGroupTaxComponent.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_taxes_group_tax_associations import GetTaxesGroupTaxAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesGroupTaxAssociations from a JSON string
get_taxes_group_tax_associations_instance = GetTaxesGroupTaxAssociations.from_json(json)
# print the JSON string representation of the object
print(GetTaxesGroupTaxAssociations.to_json())

# convert the object into a dict
get_taxes_group_tax_associations_dict = get_taxes_group_tax_associations_instance.to_dict()
# create an instance of GetTaxesGroupTaxAssociations from a dict
get_taxes_group_tax_associations_from_dict = GetTaxesGroupTaxAssociations.from_dict(get_taxes_group_tax_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


