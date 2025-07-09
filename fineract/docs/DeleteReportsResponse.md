# DeleteReportsResponse

DeleteReportsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.delete_reports_response import DeleteReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteReportsResponse from a JSON string
delete_reports_response_instance = DeleteReportsResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteReportsResponse.to_json())

# convert the object into a dict
delete_reports_response_dict = delete_reports_response_instance.to_dict()
# create an instance of DeleteReportsResponse from a dict
delete_reports_response_from_dict = DeleteReportsResponse.from_dict(delete_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


