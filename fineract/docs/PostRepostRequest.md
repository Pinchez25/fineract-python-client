# PostRepostRequest

PostRepostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**report_category** | **str** |  | [optional] 
**report_name** | **str** |  | [optional] 
**report_parameters** | **List[object]** |  | [optional] 
**report_sql** | **str** |  | [optional] 
**report_sub_type** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_repost_request import PostRepostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRepostRequest from a JSON string
post_repost_request_instance = PostRepostRequest.from_json(json)
# print the JSON string representation of the object
print PostRepostRequest.to_json()

# convert the object into a dict
post_repost_request_dict = post_repost_request_instance.to_dict()
# create an instance of PostRepostRequest from a dict
post_repost_request_form_dict = post_repost_request.from_dict(post_repost_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


