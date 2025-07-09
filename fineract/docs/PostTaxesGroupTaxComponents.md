# PostTaxesGroupTaxComponents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** |  | [optional] 
**tax_component_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_taxes_group_tax_components import PostTaxesGroupTaxComponents

# TODO update the JSON string below
json = "{}"
# create an instance of PostTaxesGroupTaxComponents from a JSON string
post_taxes_group_tax_components_instance = PostTaxesGroupTaxComponents.from_json(json)
# print the JSON string representation of the object
print PostTaxesGroupTaxComponents.to_json()

# convert the object into a dict
post_taxes_group_tax_components_dict = post_taxes_group_tax_components_instance.to_dict()
# create an instance of PostTaxesGroupTaxComponents from a dict
post_taxes_group_tax_components_form_dict = post_taxes_group_tax_components.from_dict(post_taxes_group_tax_components_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


