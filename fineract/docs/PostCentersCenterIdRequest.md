# PostCentersCenterIdRequest

PostCentersCenterIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closure_date** | **str** |  | [optional] 
**closure_reason_id** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_centers_center_id_request import PostCentersCenterIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCentersCenterIdRequest from a JSON string
post_centers_center_id_request_instance = PostCentersCenterIdRequest.from_json(json)
# print the JSON string representation of the object
print PostCentersCenterIdRequest.to_json()

# convert the object into a dict
post_centers_center_id_request_dict = post_centers_center_id_request_instance.to_dict()
# create an instance of PostCentersCenterIdRequest from a dict
post_centers_center_id_request_form_dict = post_centers_center_id_request.from_dict(post_centers_center_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


