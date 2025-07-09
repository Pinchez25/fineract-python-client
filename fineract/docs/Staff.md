# Staff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**joining_date** | **date** |  | [optional] 
**lastname** | **str** |  | [optional] 
**loan_officer** | **bool** |  | [optional] 
**mobile_no** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**not_active** | **bool** |  | [optional] 
**not_loan_officer** | **bool** |  | [optional] 
**office** | [**Office**](Office.md) |  | [optional] 
**organisational_role_parent_staff** | [**Staff**](Staff.md) |  | [optional] 
**organisational_role_type** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.staff import Staff

# TODO update the JSON string below
json = "{}"
# create an instance of Staff from a JSON string
staff_instance = Staff.from_json(json)
# print the JSON string representation of the object
print(Staff.to_json())

# convert the object into a dict
staff_dict = staff_instance.to_dict()
# create an instance of Staff from a dict
staff_from_dict = Staff.from_dict(staff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


