# PutTaxesGroupTaxGroupIdRequest

PutTaxesGroupTaxGroupIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tax_components** | [**List[PutTaxesGroupTaxComponents]**](PutTaxesGroupTaxComponents.md) |  | [optional] 

## Example

```python
from fineract_client.models.put_taxes_group_tax_group_id_request import PutTaxesGroupTaxGroupIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutTaxesGroupTaxGroupIdRequest from a JSON string
put_taxes_group_tax_group_id_request_instance = PutTaxesGroupTaxGroupIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutTaxesGroupTaxGroupIdRequest.to_json())

# convert the object into a dict
put_taxes_group_tax_group_id_request_dict = put_taxes_group_tax_group_id_request_instance.to_dict()
# create an instance of PutTaxesGroupTaxGroupIdRequest from a dict
put_taxes_group_tax_group_id_request_from_dict = PutTaxesGroupTaxGroupIdRequest.from_dict(put_taxes_group_tax_group_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


