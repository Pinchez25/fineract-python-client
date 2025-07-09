# PostFundsRequest

PostFundsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_funds_request import PostFundsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFundsRequest from a JSON string
post_funds_request_instance = PostFundsRequest.from_json(json)
# print the JSON string representation of the object
print PostFundsRequest.to_json()

# convert the object into a dict
post_funds_request_dict = post_funds_request_instance.to_dict()
# create an instance of PostFundsRequest from a dict
post_funds_request_form_dict = post_funds_request.from_dict(post_funds_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


