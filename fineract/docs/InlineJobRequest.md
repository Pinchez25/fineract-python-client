# InlineJobRequest

InlineJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loan_ids** | **List[int]** |  | [optional] 

## Example

```python
from fineract_client.models.inline_job_request import InlineJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InlineJobRequest from a JSON string
inline_job_request_instance = InlineJobRequest.from_json(json)
# print the JSON string representation of the object
print InlineJobRequest.to_json()

# convert the object into a dict
inline_job_request_dict = inline_job_request_instance.to_dict()
# create an instance of InlineJobRequest from a dict
inline_job_request_form_dict = inline_job_request.from_dict(inline_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


