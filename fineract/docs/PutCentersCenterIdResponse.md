# PutCentersCenterIdResponse

PutCentersCenterIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**PutCentersChanges**](PutCentersChanges.md) |  | [optional] 
**group_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.put_centers_center_id_response import PutCentersCenterIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutCentersCenterIdResponse from a JSON string
put_centers_center_id_response_instance = PutCentersCenterIdResponse.from_json(json)
# print the JSON string representation of the object
print PutCentersCenterIdResponse.to_json()

# convert the object into a dict
put_centers_center_id_response_dict = put_centers_center_id_response_instance.to_dict()
# create an instance of PutCentersCenterIdResponse from a dict
put_centers_center_id_response_form_dict = put_centers_center_id_response.from_dict(put_centers_center_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


