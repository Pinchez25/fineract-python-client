# TaxComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **int** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**credit_account_type** | **int** |  | [optional] 
**credit_acount** | [**GLAccount**](GLAccount.md) |  | [optional] 
**debit_account_type** | **int** |  | [optional] 
**debit_acount** | [**GLAccount**](GLAccount.md) |  | [optional] 
**id** | **int** |  | [optional] 
**last_modified_by** | **int** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**new** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 
**tax_component_histories** | [**List[TaxComponentHistory]**](TaxComponentHistory.md) |  | [optional] 
**tax_group_mappings** | [**List[TaxGroupMappings]**](TaxGroupMappings.md) |  | [optional] 

## Example

```python
from fineract_client.models.tax_component import TaxComponent

# TODO update the JSON string below
json = "{}"
# create an instance of TaxComponent from a JSON string
tax_component_instance = TaxComponent.from_json(json)
# print the JSON string representation of the object
print TaxComponent.to_json()

# convert the object into a dict
tax_component_dict = tax_component_instance.to_dict()
# create an instance of TaxComponent from a dict
tax_component_form_dict = tax_component.from_dict(tax_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


