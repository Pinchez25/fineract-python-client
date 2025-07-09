# GetTaxesGroupResponse

GetTaxesGroupResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**tax_associations** | [**List[GetTaxesGroupTaxAssociations]**](GetTaxesGroupTaxAssociations.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_taxes_group_response import GetTaxesGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaxesGroupResponse from a JSON string
get_taxes_group_response_instance = GetTaxesGroupResponse.from_json(json)
# print the JSON string representation of the object
print GetTaxesGroupResponse.to_json()

# convert the object into a dict
get_taxes_group_response_dict = get_taxes_group_response_instance.to_dict()
# create an instance of GetTaxesGroupResponse from a dict
get_taxes_group_response_form_dict = get_taxes_group_response.from_dict(get_taxes_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


