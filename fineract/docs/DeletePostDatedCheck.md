# DeletePostDatedCheck

DeletePostDatedCheck

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_post_dated_check import DeletePostDatedCheck

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePostDatedCheck from a JSON string
delete_post_dated_check_instance = DeletePostDatedCheck.from_json(json)
# print the JSON string representation of the object
print DeletePostDatedCheck.to_json()

# convert the object into a dict
delete_post_dated_check_dict = delete_post_dated_check_instance.to_dict()
# create an instance of DeletePostDatedCheck from a dict
delete_post_dated_check_form_dict = delete_post_dated_check.from_dict(delete_post_dated_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


