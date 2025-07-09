# PostCentersRequest

PostCentersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_centers_request import PostCentersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCentersRequest from a JSON string
post_centers_request_instance = PostCentersRequest.from_json(json)
# print the JSON string representation of the object
print PostCentersRequest.to_json()

# convert the object into a dict
post_centers_request_dict = post_centers_request_instance.to_dict()
# create an instance of PostCentersRequest from a dict
post_centers_request_form_dict = post_centers_request.from_dict(post_centers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


