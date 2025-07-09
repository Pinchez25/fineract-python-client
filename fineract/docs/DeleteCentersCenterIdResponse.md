# DeleteCentersCenterIdResponse

DeleteCentersCenterIdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **object** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_centers_center_id_response import DeleteCentersCenterIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCentersCenterIdResponse from a JSON string
delete_centers_center_id_response_instance = DeleteCentersCenterIdResponse.from_json(json)
# print the JSON string representation of the object
print DeleteCentersCenterIdResponse.to_json()

# convert the object into a dict
delete_centers_center_id_response_dict = delete_centers_center_id_response_instance.to_dict()
# create an instance of DeleteCentersCenterIdResponse from a dict
delete_centers_center_id_response_form_dict = delete_centers_center_id_response.from_dict(delete_centers_center_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


