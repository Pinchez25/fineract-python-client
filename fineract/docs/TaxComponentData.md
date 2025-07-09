# TaxComponentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_account** | [**GLAccountData**](GLAccountData.md) |  | [optional] 
**credit_account_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**debit_account** | [**GLAccountData**](GLAccountData.md) |  | [optional] 
**debit_account_type** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**gl_account_options** | **Dict[str, List[GLAccountData]]** |  | [optional] 
**gl_account_type_options** | [**List[EnumOptionData]**](EnumOptionData.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**percentage** | **float** |  | [optional] 
**start_date** | **date** |  | [optional] 
**tax_component_histories** | [**List[TaxComponentHistoryData]**](TaxComponentHistoryData.md) |  | [optional] 

## Example

```python
from fineract_client.models.tax_component_data import TaxComponentData

# TODO update the JSON string below
json = "{}"
# create an instance of TaxComponentData from a JSON string
tax_component_data_instance = TaxComponentData.from_json(json)
# print the JSON string representation of the object
print TaxComponentData.to_json()

# convert the object into a dict
tax_component_data_dict = tax_component_data_instance.to_dict()
# create an instance of TaxComponentData from a dict
tax_component_data_form_dict = tax_component_data.from_dict(tax_component_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


