# SavingsAccountStatusEnumData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**matured** | **bool** |  | [optional] 
**premature_closed** | **bool** |  | [optional] 
**rejected** | **bool** |  | [optional] 
**submitted_and_pending_approval** | **bool** |  | [optional] 
**transfer_in_progress** | **bool** |  | [optional] 
**transfer_on_hold** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**withdrawn_by_applicant** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.savings_account_status_enum_data import SavingsAccountStatusEnumData

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsAccountStatusEnumData from a JSON string
savings_account_status_enum_data_instance = SavingsAccountStatusEnumData.from_json(json)
# print the JSON string representation of the object
print SavingsAccountStatusEnumData.to_json()

# convert the object into a dict
savings_account_status_enum_data_dict = savings_account_status_enum_data_instance.to_dict()
# create an instance of SavingsAccountStatusEnumData from a dict
savings_account_status_enum_data_form_dict = savings_account_status_enum_data.from_dict(savings_account_status_enum_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


