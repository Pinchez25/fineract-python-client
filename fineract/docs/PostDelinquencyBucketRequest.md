# PostDelinquencyBucketRequest

PostDelinquencyBucketRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ranges** | **List[int]** |  | [optional] 

## Example

```python
from fineract_client.models.post_delinquency_bucket_request import PostDelinquencyBucketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDelinquencyBucketRequest from a JSON string
post_delinquency_bucket_request_instance = PostDelinquencyBucketRequest.from_json(json)
# print the JSON string representation of the object
print(PostDelinquencyBucketRequest.to_json())

# convert the object into a dict
post_delinquency_bucket_request_dict = post_delinquency_bucket_request_instance.to_dict()
# create an instance of PostDelinquencyBucketRequest from a dict
post_delinquency_bucket_request_from_dict = PostDelinquencyBucketRequest.from_dict(post_delinquency_bucket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


