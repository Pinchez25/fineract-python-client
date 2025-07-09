# PostCodesRequest

PostCodesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from fineract_client.models.post_codes_request import PostCodesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCodesRequest from a JSON string
post_codes_request_instance = PostCodesRequest.from_json(json)
# print the JSON string representation of the object
print PostCodesRequest.to_json()

# convert the object into a dict
post_codes_request_dict = post_codes_request_instance.to_dict()
# create an instance of PostCodesRequest from a dict
post_codes_request_form_dict = post_codes_request.from_dict(post_codes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


