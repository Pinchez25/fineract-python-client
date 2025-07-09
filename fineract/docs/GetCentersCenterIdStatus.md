# GetCentersCenterIdStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 
**closed** | **bool** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**premature_closed** | **bool** |  | [optional] 
**rejected** | **bool** |  | [optional] 
**submitted_and_pending_approval** | **bool** |  | [optional] 
**transfer_in_progress** | **bool** |  | [optional] 
**transfer_on_hold** | **bool** |  | [optional] 
**withdrawn_by_applicant** | **bool** |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_center_id_status import GetCentersCenterIdStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersCenterIdStatus from a JSON string
get_centers_center_id_status_instance = GetCentersCenterIdStatus.from_json(json)
# print the JSON string representation of the object
print(GetCentersCenterIdStatus.to_json())

# convert the object into a dict
get_centers_center_id_status_dict = get_centers_center_id_status_instance.to_dict()
# create an instance of GetCentersCenterIdStatus from a dict
get_centers_center_id_status_from_dict = GetCentersCenterIdStatus.from_dict(get_centers_center_id_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


