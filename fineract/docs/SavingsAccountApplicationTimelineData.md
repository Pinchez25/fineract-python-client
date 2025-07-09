# SavingsAccountApplicationTimelineData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_by_firstname** | **str** |  | [optional] 
**activated_by_lastname** | **str** |  | [optional] 
**activated_by_username** | **str** |  | [optional] 
**activated_on_date** | **date** |  | [optional] 
**approved_by_firstname** | **str** |  | [optional] 
**approved_by_lastname** | **str** |  | [optional] 
**approved_by_username** | **str** |  | [optional] 
**approved_on_date** | **date** |  | [optional] 
**closed_by_firstname** | **str** |  | [optional] 
**closed_by_lastname** | **str** |  | [optional] 
**closed_by_username** | **str** |  | [optional] 
**closed_on_date** | **date** |  | [optional] 
**rejected_by_firstname** | **str** |  | [optional] 
**rejected_by_lastname** | **str** |  | [optional] 
**rejected_by_username** | **str** |  | [optional] 
**rejected_on_date** | **date** |  | [optional] 
**submitted_by_firstname** | **str** |  | [optional] 
**submitted_by_lastname** | **str** |  | [optional] 
**submitted_by_username** | **str** |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**withdrawn_by_firstname** | **str** |  | [optional] 
**withdrawn_by_lastname** | **str** |  | [optional] 
**withdrawn_by_username** | **str** |  | [optional] 
**withdrawn_on_date** | **date** |  | [optional] 

## Example

```python
from fineract_client.models.savings_account_application_timeline_data import SavingsAccountApplicationTimelineData

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsAccountApplicationTimelineData from a JSON string
savings_account_application_timeline_data_instance = SavingsAccountApplicationTimelineData.from_json(json)
# print the JSON string representation of the object
print SavingsAccountApplicationTimelineData.to_json()

# convert the object into a dict
savings_account_application_timeline_data_dict = savings_account_application_timeline_data_instance.to_dict()
# create an instance of SavingsAccountApplicationTimelineData from a dict
savings_account_application_timeline_data_form_dict = savings_account_application_timeline_data.from_dict(savings_account_application_timeline_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


