# CenterData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**collection_meeting_calendar** | [**CalendarData**](CalendarData.md) |  | [optional] 
**datatables** | [**List[DatatableData]**](DatatableData.md) |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**office_name** | **str** |  | [optional] 
**row_index** | **int** |  | [optional] 
**staff_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.center_data import CenterData

# TODO update the JSON string below
json = "{}"
# create an instance of CenterData from a JSON string
center_data_instance = CenterData.from_json(json)
# print the JSON string representation of the object
print CenterData.to_json()

# convert the object into a dict
center_data_dict = center_data_instance.to_dict()
# create an instance of CenterData from a dict
center_data_form_dict = center_data.from_dict(center_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


