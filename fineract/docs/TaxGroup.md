# TaxGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **int** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**last_modified_by** | **int** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**tax_group_mappings** | [**List[TaxGroupMappings]**](TaxGroupMappings.md) |  | [optional] 

## Example

```python
from fineract_client.models.tax_group import TaxGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TaxGroup from a JSON string
tax_group_instance = TaxGroup.from_json(json)
# print the JSON string representation of the object
print(TaxGroup.to_json())

# convert the object into a dict
tax_group_dict = tax_group_instance.to_dict()
# create an instance of TaxGroup from a dict
tax_group_from_dict = TaxGroup.from_dict(tax_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


