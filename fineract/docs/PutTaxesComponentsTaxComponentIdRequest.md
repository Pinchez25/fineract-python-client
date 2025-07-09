# PutTaxesComponentsTaxComponentIdRequest

PutTaxesComponentsTaxComponentIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**percentage** | **float** |  | [optional] 
**start_date** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_taxes_components_tax_component_id_request import PutTaxesComponentsTaxComponentIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutTaxesComponentsTaxComponentIdRequest from a JSON string
put_taxes_components_tax_component_id_request_instance = PutTaxesComponentsTaxComponentIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutTaxesComponentsTaxComponentIdRequest.to_json())

# convert the object into a dict
put_taxes_components_tax_component_id_request_dict = put_taxes_components_tax_component_id_request_instance.to_dict()
# create an instance of PutTaxesComponentsTaxComponentIdRequest from a dict
put_taxes_components_tax_component_id_request_from_dict = PutTaxesComponentsTaxComponentIdRequest.from_dict(put_taxes_components_tax_component_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


