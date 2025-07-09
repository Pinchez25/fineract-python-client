# PostOfficesResponse

PostOfficesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**office_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_offices_response import PostOfficesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostOfficesResponse from a JSON string
post_offices_response_instance = PostOfficesResponse.from_json(json)
# print the JSON string representation of the object
print PostOfficesResponse.to_json()

# convert the object into a dict
post_offices_response_dict = post_offices_response_instance.to_dict()
# create an instance of PostOfficesResponse from a dict
post_offices_response_form_dict = post_offices_response.from_dict(post_offices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


