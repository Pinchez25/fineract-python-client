# RetrieveOneResponse

GetStaffResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**firstname** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_loan_officer** | **bool** |  | [optional] 
**joining_date** | **date** |  | [optional] 
**lastname** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.retrieve_one_response import RetrieveOneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveOneResponse from a JSON string
retrieve_one_response_instance = RetrieveOneResponse.from_json(json)
# print the JSON string representation of the object
print RetrieveOneResponse.to_json()

# convert the object into a dict
retrieve_one_response_dict = retrieve_one_response_instance.to_dict()
# create an instance of RetrieveOneResponse from a dict
retrieve_one_response_form_dict = retrieve_one_response.from_dict(retrieve_one_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


