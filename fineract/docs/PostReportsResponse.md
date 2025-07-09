# PostReportsResponse

PostReportsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_reports_response import PostReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostReportsResponse from a JSON string
post_reports_response_instance = PostReportsResponse.from_json(json)
# print the JSON string representation of the object
print PostReportsResponse.to_json()

# convert the object into a dict
post_reports_response_dict = post_reports_response_instance.to_dict()
# create an instance of PostReportsResponse from a dict
post_reports_response_form_dict = post_reports_response.from_dict(post_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


