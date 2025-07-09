# PutTaxesComponentsTaxComponentIdResponse

PutTaxesComponentsTaxComponentIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutTaxesComponentsChanges**](PutTaxesComponentsChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_taxes_components_tax_component_id_response import PutTaxesComponentsTaxComponentIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutTaxesComponentsTaxComponentIdResponse from a JSON string
put_taxes_components_tax_component_id_response_instance = PutTaxesComponentsTaxComponentIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutTaxesComponentsTaxComponentIdResponse.to_json())

# convert the object into a dict
put_taxes_components_tax_component_id_response_dict = put_taxes_components_tax_component_id_response_instance.to_dict()
# create an instance of PutTaxesComponentsTaxComponentIdResponse from a dict
put_taxes_components_tax_component_id_response_from_dict = PutTaxesComponentsTaxComponentIdResponse.from_dict(put_taxes_components_tax_component_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


