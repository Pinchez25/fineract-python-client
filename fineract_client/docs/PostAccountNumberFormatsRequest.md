# PostAccountNumberFormatsRequest

PostAccountNumberFormatsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **int** |  | [optional] 
**prefix_type** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_account_number_formats_request import PostAccountNumberFormatsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAccountNumberFormatsRequest from a JSON string
post_account_number_formats_request_instance = PostAccountNumberFormatsRequest.from_json(json)
# print the JSON string representation of the object
print(PostAccountNumberFormatsRequest.to_json())

# convert the object into a dict
post_account_number_formats_request_dict = post_account_number_formats_request_instance.to_dict()
# create an instance of PostAccountNumberFormatsRequest from a dict
post_account_number_formats_request_from_dict = PostAccountNumberFormatsRequest.from_dict(post_account_number_formats_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


