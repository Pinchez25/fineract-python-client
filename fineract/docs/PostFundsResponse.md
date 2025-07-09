# PostFundsResponse

PostFundsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_funds_response import PostFundsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostFundsResponse from a JSON string
post_funds_response_instance = PostFundsResponse.from_json(json)
# print the JSON string representation of the object
print(PostFundsResponse.to_json())

# convert the object into a dict
post_funds_response_dict = post_funds_response_instance.to_dict()
# create an instance of PostFundsResponse from a dict
post_funds_response_from_dict = PostFundsResponse.from_dict(post_funds_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


