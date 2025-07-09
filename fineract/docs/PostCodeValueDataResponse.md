# PostCodeValueDataResponse

PostCodeValueDataResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_code_value_data_response import PostCodeValueDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCodeValueDataResponse from a JSON string
post_code_value_data_response_instance = PostCodeValueDataResponse.from_json(json)
# print the JSON string representation of the object
print(PostCodeValueDataResponse.to_json())

# convert the object into a dict
post_code_value_data_response_dict = post_code_value_data_response_instance.to_dict()
# create an instance of PostCodeValueDataResponse from a dict
post_code_value_data_response_from_dict = PostCodeValueDataResponse.from_dict(post_code_value_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


