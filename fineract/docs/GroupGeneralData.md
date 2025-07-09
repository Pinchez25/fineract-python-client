# GroupGeneralData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_no** | **str** |  | [optional] 
**activation_date** | **date** |  | [optional] 
**active** | **bool** |  | [optional] 
**active_client_members** | [**List[ClientData]**](ClientData.md) |  | [optional] 
**available_roles** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**calendars_data** | [**List[CalendarData]**](CalendarData.md) |  | [optional] 
**center_id** | **int** |  | [optional] 
**center_name** | **str** |  | [optional] 
**center_options** | [**List[CenterData]**](CenterData.md) |  | [optional] 
**child_group** | **bool** |  | [optional] 
**client_members** | [**List[ClientData]**](ClientData.md) |  | [optional] 
**client_options** | [**List[ClientData]**](ClientData.md) |  | [optional] 
**closure_reasons** | [**List[CodeValueData]**](CodeValueData.md) |  | [optional] 
**collection_meeting_calendar** | [**CalendarData**](CalendarData.md) |  | [optional] 
**datatables** | [**List[DatatableData]**](DatatableData.md) |  | [optional] 
**date_format** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**group_level** | **str** |  | [optional] 
**group_roles** | [**List[GroupRoleData]**](GroupRoleData.md) |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**office_options** | [**List[OfficeData]**](OfficeData.md) |  | [optional] 
**parent_id** | **int** |  | [optional] 
**row_index** | **int** |  | [optional] 
**selected_role** | [**GroupRoleData**](GroupRoleData.md) |  | [optional] 
**staff_id** | **int** |  | [optional] 
**staff_name** | **str** |  | [optional] 
**staff_options** | [**List[StaffData]**](StaffData.md) |  | [optional] 
**status** | [**EnumOptionData**](EnumOptionData.md) |  | [optional] 
**submitted_on_date** | **date** |  | [optional] 
**timeline** | **object** |  | [optional] 

## Example

```python
from fineract_client.models.group_general_data import GroupGeneralData

# TODO update the JSON string below
json = "{}"
# create an instance of GroupGeneralData from a JSON string
group_general_data_instance = GroupGeneralData.from_json(json)
# print the JSON string representation of the object
print GroupGeneralData.to_json()

# convert the object into a dict
group_general_data_dict = group_general_data_instance.to_dict()
# create an instance of GroupGeneralData from a dict
group_general_data_form_dict = group_general_data.from_dict(group_general_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


