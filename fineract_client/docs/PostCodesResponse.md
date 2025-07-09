# PostCodesResponse

PostCodesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_codes_response import PostCodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCodesResponse from a JSON string
post_codes_response_instance = PostCodesResponse.from_json(json)
# print the JSON string representation of the object
print(PostCodesResponse.to_json())

# convert the object into a dict
post_codes_response_dict = post_codes_response_instance.to_dict()
# create an instance of PostCodesResponse from a dict
post_codes_response_from_dict = PostCodesResponse.from_dict(post_codes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


