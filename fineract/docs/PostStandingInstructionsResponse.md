# PostStandingInstructionsResponse

PostStandingInstructionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_standing_instructions_response import PostStandingInstructionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostStandingInstructionsResponse from a JSON string
post_standing_instructions_response_instance = PostStandingInstructionsResponse.from_json(json)
# print the JSON string representation of the object
print PostStandingInstructionsResponse.to_json()

# convert the object into a dict
post_standing_instructions_response_dict = post_standing_instructions_response_instance.to_dict()
# create an instance of PostStandingInstructionsResponse from a dict
post_standing_instructions_response_form_dict = post_standing_instructions_response.from_dict(post_standing_instructions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


