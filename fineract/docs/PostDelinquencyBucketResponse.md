# PostDelinquencyBucketResponse

PostDelinquencyBucketResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 

## Example

```python
from fineract_client.models.post_delinquency_bucket_response import PostDelinquencyBucketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostDelinquencyBucketResponse from a JSON string
post_delinquency_bucket_response_instance = PostDelinquencyBucketResponse.from_json(json)
# print the JSON string representation of the object
print(PostDelinquencyBucketResponse.to_json())

# convert the object into a dict
post_delinquency_bucket_response_dict = post_delinquency_bucket_response_instance.to_dict()
# create an instance of PostDelinquencyBucketResponse from a dict
post_delinquency_bucket_response_from_dict = PostDelinquencyBucketResponse.from_dict(post_delinquency_bucket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


