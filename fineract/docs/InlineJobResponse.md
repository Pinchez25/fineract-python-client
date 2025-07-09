# InlineJobResponse

InlineJobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_ids** | **List[int]** |  | [optional] 

## Example

```python
from fineract_client.models.inline_job_response import InlineJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InlineJobResponse from a JSON string
inline_job_response_instance = InlineJobResponse.from_json(json)
# print the JSON string representation of the object
print InlineJobResponse.to_json()

# convert the object into a dict
inline_job_response_dict = inline_job_response_instance.to_dict()
# create an instance of InlineJobResponse from a dict
inline_job_response_form_dict = inline_job_response.from_dict(inline_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


