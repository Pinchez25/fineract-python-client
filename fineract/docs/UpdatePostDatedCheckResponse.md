# UpdatePostDatedCheckResponse

UpdatePostDatedCheckResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**UpdateChangesResponse**](UpdateChangesResponse.md) |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.update_post_dated_check_response import UpdatePostDatedCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePostDatedCheckResponse from a JSON string
update_post_dated_check_response_instance = UpdatePostDatedCheckResponse.from_json(json)
# print the JSON string representation of the object
print UpdatePostDatedCheckResponse.to_json()

# convert the object into a dict
update_post_dated_check_response_dict = update_post_dated_check_response_instance.to_dict()
# create an instance of UpdatePostDatedCheckResponse from a dict
update_post_dated_check_response_form_dict = update_post_dated_check_response.from_dict(update_post_dated_check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


