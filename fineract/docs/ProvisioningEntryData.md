# ProvisioningEntryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_id** | **int** |  | [optional] 
**created_date** | **date** |  | [optional] 
**created_user** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**journal_entry** | **bool** |  | [optional] 
**modified_by_id** | **int** |  | [optional] 
**modified_user** | **str** |  | [optional] 
**provisioning_entries** | [**List[LoanProductProvisioningEntryData]**](LoanProductProvisioningEntryData.md) |  | [optional] 
**reserved_amount** | **float** |  | [optional] 

## Example

```python
from fineract_client.models.provisioning_entry_data import ProvisioningEntryData

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningEntryData from a JSON string
provisioning_entry_data_instance = ProvisioningEntryData.from_json(json)
# print the JSON string representation of the object
print(ProvisioningEntryData.to_json())

# convert the object into a dict
provisioning_entry_data_dict = provisioning_entry_data_instance.to_dict()
# create an instance of ProvisioningEntryData from a dict
provisioning_entry_data_from_dict = ProvisioningEntryData.from_dict(provisioning_entry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


