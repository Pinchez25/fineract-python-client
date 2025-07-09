# PostCentersResponse

PostCentersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** |  | [optional] 
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_centers_response import PostCentersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCentersResponse from a JSON string
post_centers_response_instance = PostCentersResponse.from_json(json)
# print the JSON string representation of the object
print PostCentersResponse.to_json()

# convert the object into a dict
post_centers_response_dict = post_centers_response_instance.to_dict()
# create an instance of PostCentersResponse from a dict
post_centers_response_form_dict = post_centers_response.from_dict(post_centers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


