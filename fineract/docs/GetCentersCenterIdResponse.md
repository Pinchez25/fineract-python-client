# GetCentersCenterIdResponse

GetCentersCenterIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**hierarchy** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**office_name** | **str** |  | [optional] 
**status** | [**GetCentersStatus**](GetCentersStatus.md) |  | [optional] 

## Example

```python
from fineract_client.models.get_centers_center_id_response import GetCentersCenterIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCentersCenterIdResponse from a JSON string
get_centers_center_id_response_instance = GetCentersCenterIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetCentersCenterIdResponse.to_json())

# convert the object into a dict
get_centers_center_id_response_dict = get_centers_center_id_response_instance.to_dict()
# create an instance of GetCentersCenterIdResponse from a dict
get_centers_center_id_response_from_dict = GetCentersCenterIdResponse.from_dict(get_centers_center_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


