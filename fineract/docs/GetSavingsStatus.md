# GetSavingsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**rejected** | **bool** |  | [optional] 
**submitted_and_pending_approval** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 
**withdrawn_by_applicant** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_savings_status import GetSavingsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavingsStatus from a JSON string
get_savings_status_instance = GetSavingsStatus.from_json(json)
# print the JSON string representation of the object
print GetSavingsStatus.to_json()

# convert the object into a dict
get_savings_status_dict = get_savings_status_instance.to_dict()
# create an instance of GetSavingsStatus from a dict
get_savings_status_form_dict = get_savings_status.from_dict(get_savings_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


