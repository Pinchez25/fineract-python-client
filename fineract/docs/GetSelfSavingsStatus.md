# GetSelfSavingsStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**rejected** | **bool** |  | [optional] 
**submitted_and_pending_approval** | **bool** |  | [optional] 
**withdrawn_by_applicant** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_self_savings_status import GetSelfSavingsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetSelfSavingsStatus from a JSON string
get_self_savings_status_instance = GetSelfSavingsStatus.from_json(json)
# print the JSON string representation of the object
print GetSelfSavingsStatus.to_json()

# convert the object into a dict
get_self_savings_status_dict = get_self_savings_status_instance.to_dict()
# create an instance of GetSelfSavingsStatus from a dict
get_self_savings_status_form_dict = get_self_savings_status.from_dict(get_self_savings_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


