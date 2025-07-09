# StaffData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**joining_date** | **date** |  | [optional] 
**lastname** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**row_index** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.staff_data import StaffData

# TODO update the JSON string below
json = "{}"
# create an instance of StaffData from a JSON string
staff_data_instance = StaffData.from_json(json)
# print the JSON string representation of the object
print StaffData.to_json()

# convert the object into a dict
staff_data_dict = staff_data_instance.to_dict()
# create an instance of StaffData from a dict
staff_data_form_dict = staff_data.from_dict(staff_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


