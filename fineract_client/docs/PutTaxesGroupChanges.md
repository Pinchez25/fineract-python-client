# PutTaxesGroupChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_components** | **List[int]** |  | [optional] 
**modified_components** | [**List[PutTaxesGroupModifiedComponents]**](PutTaxesGroupModifiedComponents.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.put_taxes_group_changes import PutTaxesGroupChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutTaxesGroupChanges from a JSON string
put_taxes_group_changes_instance = PutTaxesGroupChanges.from_json(json)
# print the JSON string representation of the object
print(PutTaxesGroupChanges.to_json())

# convert the object into a dict
put_taxes_group_changes_dict = put_taxes_group_changes_instance.to_dict()
# create an instance of PutTaxesGroupChanges from a dict
put_taxes_group_changes_from_dict = PutTaxesGroupChanges.from_dict(put_taxes_group_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


