# PutTaxesComponentsChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**percentage** | **float** |  | [optional] 
**start_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.put_taxes_components_changes import PutTaxesComponentsChanges

# TODO update the JSON string below
json = "{}"
# create an instance of PutTaxesComponentsChanges from a JSON string
put_taxes_components_changes_instance = PutTaxesComponentsChanges.from_json(json)
# print the JSON string representation of the object
print(PutTaxesComponentsChanges.to_json())

# convert the object into a dict
put_taxes_components_changes_dict = put_taxes_components_changes_instance.to_dict()
# create an instance of PutTaxesComponentsChanges from a dict
put_taxes_components_changes_from_dict = PutTaxesComponentsChanges.from_dict(put_taxes_components_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


