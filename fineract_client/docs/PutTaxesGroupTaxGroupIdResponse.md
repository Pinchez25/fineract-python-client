# PutTaxesGroupTaxGroupIdResponse

PutTaxesGroupTaxGroupIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutTaxesGroupChanges**](PutTaxesGroupChanges.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_taxes_group_tax_group_id_response import PutTaxesGroupTaxGroupIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutTaxesGroupTaxGroupIdResponse from a JSON string
put_taxes_group_tax_group_id_response_instance = PutTaxesGroupTaxGroupIdResponse.from_json(json)
# print the JSON string representation of the object
print(PutTaxesGroupTaxGroupIdResponse.to_json())

# convert the object into a dict
put_taxes_group_tax_group_id_response_dict = put_taxes_group_tax_group_id_response_instance.to_dict()
# create an instance of PutTaxesGroupTaxGroupIdResponse from a dict
put_taxes_group_tax_group_id_response_from_dict = PutTaxesGroupTaxGroupIdResponse.from_dict(put_taxes_group_tax_group_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


