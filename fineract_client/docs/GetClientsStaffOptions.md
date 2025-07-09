# GetClientsStaffOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_loan_officer** | **bool** |  | [optional] 
**lastname** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.get_clients_staff_options import GetClientsStaffOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientsStaffOptions from a JSON string
get_clients_staff_options_instance = GetClientsStaffOptions.from_json(json)
# print the JSON string representation of the object
print(GetClientsStaffOptions.to_json())

# convert the object into a dict
get_clients_staff_options_dict = get_clients_staff_options_instance.to_dict()
# create an instance of GetClientsStaffOptions from a dict
get_clients_staff_options_from_dict = GetClientsStaffOptions.from_dict(get_clients_staff_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


