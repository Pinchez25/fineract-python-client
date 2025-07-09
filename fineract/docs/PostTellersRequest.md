# PostTellersRequest

PostTellersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**office_id** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_tellers_request import PostTellersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTellersRequest from a JSON string
post_tellers_request_instance = PostTellersRequest.from_json(json)
# print the JSON string representation of the object
print(PostTellersRequest.to_json())

# convert the object into a dict
post_tellers_request_dict = post_tellers_request_instance.to_dict()
# create an instance of PostTellersRequest from a dict
post_tellers_request_from_dict = PostTellersRequest.from_dict(post_tellers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


