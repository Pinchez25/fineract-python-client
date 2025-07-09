# PostAuthenticationRequest

PostAuthenticationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from fineract_client.models.post_authentication_request import PostAuthenticationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthenticationRequest from a JSON string
post_authentication_request_instance = PostAuthenticationRequest.from_json(json)
# print the JSON string representation of the object
print PostAuthenticationRequest.to_json()

# convert the object into a dict
post_authentication_request_dict = post_authentication_request_instance.to_dict()
# create an instance of PostAuthenticationRequest from a dict
post_authentication_request_form_dict = post_authentication_request.from_dict(post_authentication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


