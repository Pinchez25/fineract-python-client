# PutTaxesGroupModifiedComponents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** |  | [optional] 
**tax_component_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_taxes_group_modified_components import PutTaxesGroupModifiedComponents

# TODO update the JSON string below
json = "{}"
# create an instance of PutTaxesGroupModifiedComponents from a JSON string
put_taxes_group_modified_components_instance = PutTaxesGroupModifiedComponents.from_json(json)
# print the JSON string representation of the object
print(PutTaxesGroupModifiedComponents.to_json())

# convert the object into a dict
put_taxes_group_modified_components_dict = put_taxes_group_modified_components_instance.to_dict()
# create an instance of PutTaxesGroupModifiedComponents from a dict
put_taxes_group_modified_components_from_dict = PutTaxesGroupModifiedComponents.from_dict(put_taxes_group_modified_components_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


