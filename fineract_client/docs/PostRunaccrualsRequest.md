# PostRunaccrualsRequest

runaccrualsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_format** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**till_date** | **str** | which specifies periodic accruals should happen till the given Date | 

## Example

```python
from fineract_client.models.post_runaccruals_request import PostRunaccrualsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRunaccrualsRequest from a JSON string
post_runaccruals_request_instance = PostRunaccrualsRequest.from_json(json)
# print the JSON string representation of the object
print(PostRunaccrualsRequest.to_json())

# convert the object into a dict
post_runaccruals_request_dict = post_runaccruals_request_instance.to_dict()
# create an instance of PostRunaccrualsRequest from a dict
post_runaccruals_request_from_dict = PostRunaccrualsRequest.from_dict(post_runaccruals_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


