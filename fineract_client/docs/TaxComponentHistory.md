# TaxComponentHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **int** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**last_modified_by** | **int** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**new** | **bool** |  | [optional] 
**percentage** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.tax_component_history import TaxComponentHistory

# TODO update the JSON string below
json = "{}"
# create an instance of TaxComponentHistory from a JSON string
tax_component_history_instance = TaxComponentHistory.from_json(json)
# print the JSON string representation of the object
print(TaxComponentHistory.to_json())

# convert the object into a dict
tax_component_history_dict = tax_component_history_instance.to_dict()
# create an instance of TaxComponentHistory from a dict
tax_component_history_from_dict = TaxComponentHistory.from_dict(tax_component_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


