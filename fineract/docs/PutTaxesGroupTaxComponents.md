# PutTaxesGroupTaxComponents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**tax_component_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_taxes_group_tax_components import PutTaxesGroupTaxComponents

# TODO update the JSON string below
json = "{}"
# create an instance of PutTaxesGroupTaxComponents from a JSON string
put_taxes_group_tax_components_instance = PutTaxesGroupTaxComponents.from_json(json)
# print the JSON string representation of the object
print(PutTaxesGroupTaxComponents.to_json())

# convert the object into a dict
put_taxes_group_tax_components_dict = put_taxes_group_tax_components_instance.to_dict()
# create an instance of PutTaxesGroupTaxComponents from a dict
put_taxes_group_tax_components_from_dict = PutTaxesGroupTaxComponents.from_dict(put_taxes_group_tax_components_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


