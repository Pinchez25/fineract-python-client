# SavingsAccountSubStatusEnumData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | **bool** |  | [optional] 
**block_credit** | **bool** |  | [optional] 
**block_debit** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**dormant** | **bool** |  | [optional] 
**escheat** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive** | **bool** |  | [optional] 
**var_none** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.savings_account_sub_status_enum_data import SavingsAccountSubStatusEnumData

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsAccountSubStatusEnumData from a JSON string
savings_account_sub_status_enum_data_instance = SavingsAccountSubStatusEnumData.from_json(json)
# print the JSON string representation of the object
print SavingsAccountSubStatusEnumData.to_json()

# convert the object into a dict
savings_account_sub_status_enum_data_dict = savings_account_sub_status_enum_data_instance.to_dict()
# create an instance of SavingsAccountSubStatusEnumData from a dict
savings_account_sub_status_enum_data_form_dict = savings_account_sub_status_enum_data.from_dict(savings_account_sub_status_enum_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


